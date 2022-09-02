from aws_cdk import (
    CfnOutput,
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
)
from constructs import Construct

from code.asg_construct import ASG_Construct
from code.efs_construct import EFS_Construct
from code.nacl_construct import NACL_Construct
from code.s3_construct import S3_Construct
from code.backup_construct import Backup_Construct
from code.sg_construct import Admin_SG_Construct, Web_SG_Construct
from code.vpc_construct import WEB_VPC_Construct, ADMIN_VPC_Construct
from code.elb_construct import ELB_Construct

from code._config import TEST_ENV, KEY_PAIR

class IACStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create 2 VPC's and VPC peering connection
        self.vpc_web = WEB_VPC_Construct(self, 'vpc-web').vpc_web

        self.vpc_admin = ADMIN_VPC_Construct(self, 'vpc-admin').vpc_admin

        self.vpc_peer = ec2.CfnVPCPeeringConnection(
            self, 'peer_vpc_id',
            peer_vpc_id=self.vpc_admin.vpc_id,
            vpc_id=self.vpc_web.vpc_id,
        )

        # Update Route Tables for Peering Connection
        # VPC web Public
        for subnet in self.vpc_web.public_subnets:
            route_table_entry = ec2.CfnRoute(
                self, f'{subnet.node.addr}-peer-route',
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block='10.20.0.0/16',
                vpc_peering_connection_id=self.vpc_peer.ref,
            )
        # VPC web Private
        for subnet in self.vpc_web.isolated_subnets:
            route_table_entry = ec2.CfnRoute(
                self, f'{subnet.node.addr}-peer-route',
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block='10.20.0.0/16',
                vpc_peering_connection_id=self.vpc_peer.ref,
            )

        # VPC admin Public
        for subnet in self.vpc_admin.public_subnets:
            route_table_entry = ec2.CfnRoute(
                self, f'{subnet.node.addr}-peer-route',
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block='10.10.0.0/16',
                vpc_peering_connection_id=self.vpc_peer.ref,
            )

        # Add Network ACLs to the VPCs
        self.network_acl = NACL_Construct(
            self, 'NACL',
            vpc_web=self.vpc_web,
            vpc_admin=self.vpc_admin,
        )

        ####################
        ### Admin Server ###
        ####################

        self.admin_server_sg = Admin_SG_Construct(
            self, 'management-sg',
            vpc=self.vpc_admin
        )

        self.admin_server = ec2.Instance(
            self, 'management-server',
            vpc=self.vpc_admin,
            vpc_subnets=ec2.SubnetType.PUBLIC,
            security_group=self.admin_server_sg.sg,
            instance_type=ec2.InstanceType('t3.nano'),
            # machine_image=ec2.AmazonLinuxImage(
            #     generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            #     ),
            machine_image=ec2.WindowsImage(ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_CORE_BASE),
            key_name=KEY_PAIR,
            block_devices=[
                ec2.BlockDevice(
                    device_name='/dev/sda1',
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=30,
                        encrypted=True,
                        delete_on_termination=TEST_ENV
                ))],
            role=iam.Role(self, "admin-role",
                assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
                managed_policies=[
                    iam.ManagedPolicy.from_aws_managed_policy_name('AmazonSSMManagedInstanceCore')
                ],
            )
        )
        
        # Install OpenSSH on Admin Server
        self.admin_server.user_data.for_windows()
        self.admin_server.add_user_data(
            'Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0',
            'Start-Service sshd',
            "Set-Service -Name sshd -StartupType 'Automatic'",
            "New-NetFirewallRule -Name sshd -DisplayName 'Allow SSH' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22"
            )
        

        ########################
        ### Web Server Fleet ###
        ########################

        # WebServerSG
        self.web_server_sg = Web_SG_Construct(
            self, 'production-sg',
            vpc=self.vpc_web,
            trusted_source=self.admin_server_sg.sg
            )

        # WebServer Role for S3 read access
        self.web_server_role = iam.Role(
            self, 'webserver-role',
            assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3ReadOnlyAccess'),
                # iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3FullAccess'),
                iam.ManagedPolicy.from_aws_managed_policy_name('AmazonSSMManagedInstanceCore')
                ],
        )

        # Auto-Scaling Group
        self.asg = ASG_Construct(
            self, 'ASG',
            vpc_web=self.vpc_web,
            security_group=self.web_server_sg.sg,
            role=self.web_server_role
        )

        # Application Load Balancer
        self.alb = ELB_Construct(
            self, 'Web-ALB',
            vpc=self.vpc_web,
            asg=self.asg.auto_scaling_group,
        )

        #################
        ### S3 Bucket ###
        #################

        self.s3_bucket = S3_Construct(self, 'PostDeploymentScripts', resource_access=[self.web_server_role, self.admin_server.role])
        
        #######################
        ### EFS File System ###
        #######################

        self.efs = EFS_Construct(
            self, 'EFS',
            vpc=self.vpc_web
            )

        self.efs.efs.connections.allow_default_port_from(self.asg.auto_scaling_group)

        ####################
        ### ASG UserData ###
        ####################

        # download webserver script
        script_path = self.asg.auto_scaling_group.user_data.add_s3_download_command(
            bucket=self.s3_bucket.script_bucket,
            bucket_key='launch-web-server.sh',
            region=self.region
        )
        self.asg.auto_scaling_group.user_data.add_execute_file_command(file_path=script_path)

        self.asg.auto_scaling_group.user_data.add_commands(
            'yum install -y amazon-efs-utils',
            'yum install -y nfs-utils',
            'file_system_id_1=' + self.efs.efs.file_system_id,
            'efs_mount_point_1=/mnt/efs/fs1',
            'mkdir -p "${efs_mount_point_1}"',
            'test -f "/sbin/mount.efs" && echo "${file_system_id_1}:/ ${efs_mount_point_1} efs defaults,_netdev" >> /etc/fstab || " + "echo "${file_system_id_1}.efs.' + Stack.of(self).region + '.amazonaws.com:/ ${efs_mount_point_1} nfs4 nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport,_netdev 0 0" >> /etc/fstab',
            'mount -a -t efs,nfs4 defaults'
            )
        
        self.asg.auto_scaling_group.user_data.add_commands(
            "mkdir /mnt/efs/fs1/html",
            "rm -rf /var/www/html && ln -s /mnt/efs/fs1/html /var/www/html",
            )

        # download website content
        self.asg.auto_scaling_group.user_data.add_s3_download_command(
            bucket=self.s3_bucket.script_bucket,
            bucket_key='website_content.zip',
            local_file='/tmp/website_content.zip',
            region=self.region
        )
        # unzip website content
        self.asg.auto_scaling_group.user_data.add_commands("chmod 755 -R /mnt/efs/fs1/html")
        self.asg.auto_scaling_group.user_data.add_commands("unzip /tmp/website_content.zip -d /mnt/efs/fs1/html")

        ###################
        ### Backup Plan ###
        ###################
        backup_plan = Backup_Construct(
            self, 'Backup-Plan',
            efs_resources=[self.efs.efs],
        )

        CfnOutput(self, 'ALB DNS', value=self.alb.alb.load_balancer_dns_name)
        CfnOutput(self, 'MGMT IP', value=self.admin_server.instance_public_ip)

