from re import sub
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
)
from constructs import Construct

from code.nacl_construct import NACL_Construct
from code.s3_construct import S3_Construct
from code.backup_construct import Backup_Construct
from code.sg_construct import Admin_SG_Construct, Web_SG_Construct
from code.vpc_construct import WEB_VPC_Construct, ADMIN_VPC_Construct
from code.ec2_construct import EC2_Construct

from code._config import TEST_ENV, TRUSTED_IP, AVAILABILITY_ZONES

class IACStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create 2 VPC's and VPC peering connection
        self.vpc_web_all = WEB_VPC_Construct(self, 'vpc-web')
        self.vpc_web = self.vpc_web_all.vpc_web

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
        for subnet in self.vpc_web_all.private_subnet_list.values():
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
            vpc_web=self.vpc_web_all,
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
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            # machine_image=ec2.WindowsImage(ec2.WindowsVersion.WINDOWS_SERVER_2022_DUTCH_FULL_BASE),
            key_name='ec2-key-pair',
            block_devices=[
                ec2.BlockDevice(
                    device_name='/dev/xvda',
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=True,
                        delete_on_termination=TEST_ENV
                ))],
        )
        
        # ##################
        # ### Web Server ###
        # ##################

        # WebServerSG

        self.web_server_sg = Web_SG_Construct(
            self, 'production-sg',
            vpc=self.vpc_web,
            trusted_source=self.admin_server_sg.sg
            )

        #WebServer Role for S3 read access
        self.web_server_role = iam.Role(
            self, 'webserver-role',
            assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3ReadOnlyAccess')
                ],
        )

        self.web_server = ec2.Instance(
            self, 'web-server',
            vpc=self.vpc_web,
            vpc_subnets=ec2.SubnetType.PUBLIC,
            role=self.web_server_role,
            security_group=self.web_server_sg.sg,
            instance_type=ec2.InstanceType('t3.nano'),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
                ),
            key_name='ec2-key-pair',
            block_devices=[
                ec2.BlockDevice(
                    device_name='/dev/xvda',
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=True,
                        delete_on_termination=TEST_ENV,
                    )),
                ec2.BlockDevice(
                    device_name='/dev/xvdf',
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=2,
                        encrypted=True,
                        delete_on_termination=TEST_ENV,
                    ))],
        )
        
        #################
        ### S3 Bucket ###
        #################

        self.s3_bucket = S3_Construct(self, 'PostDeploymentScripts')

        ##########################
        ### WebServer UserData ###
        ##########################

        # download webserver script
        script_path = self.web_server.user_data.add_s3_download_command(
            bucket=self.s3_bucket.script_bucket,
            bucket_key='launch-web-server.sh',
        )
        self.web_server.user_data.add_execute_file_command(file_path=script_path)

        # download website content
        self.web_server.user_data.add_s3_download_command(
            bucket=self.s3_bucket.script_bucket,
            bucket_key='website_content.zip',
            local_file='/tmp/website_content.zip'
        )
        # unzip website content
        self.web_server.user_data.add_commands("chmod 755 -R /var/www/html/")
        self.web_server.user_data.add_commands("unzip /tmp/website_content.zip -d /var/www/html/")
        
        # download ebs volume partition disk
        ebs_disk_path = self.web_server.user_data.add_s3_download_command(
            bucket=self.s3_bucket.script_bucket,
            bucket_key='mount-ebs.sh'
        )
        self.web_server.user_data.add_execute_file_command(file_path=ebs_disk_path)

        # ###################
        # ### Backup Plan ###
        # ###################
        # backup_plan = Backup_Construct(
        #     self, 'Backup-Plan',
        #     instances=[self.web_server],
        # )
