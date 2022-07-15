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

from code._config import TEST_ENV, TRUSTED_IP 

class VPCStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create 2 VPC's and VPC peering connection
        vpc_web = ec2.Vpc(
            self, 'app-prd-vpc',
            cidr='10.10.10.0/24',
            max_azs=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name='Public',
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=26
                ),
                # # commented out for V1.0
                # ec2.SubnetConfiguration(
                #     name='Private',
                #     subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                #     cidr_mask=26
                # )
                ],
            )

        vpc_admin = ec2.Vpc(
            self, 'management-prd-vpc',
            cidr='10.10.20.0/24',
            max_azs=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name='Public',
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=26
                )],
            )

        vpc_peer = ec2.CfnVPCPeeringConnection(
            self, 'peer_vpc_id',
            peer_vpc_id=vpc_admin.vpc_id,
            vpc_id=vpc_web.vpc_id,
        ) 

        # Update Route Tables for Peering Connection
        for subnet in vpc_web.public_subnets:
            route_table_entry = ec2.CfnRoute(
                self, 'VPC-1 Peer Route',
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block='10.10.20.0/24',
                vpc_peering_connection_id=vpc_peer.ref,
            )

        for subnet in vpc_admin.public_subnets:
            route_table_entry = ec2.CfnRoute(
                self, 'VPC-2 Peer Route',
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block='10.10.10.0/24',
                vpc_peering_connection_id=vpc_peer.ref,
            )

        network_acl = NACL_Construct(
            self, 'NACL',
            vpc_web=vpc_web,
            vpc_admin=vpc_admin,
        )

        ####################
        ### Admin Server ###
        ####################

        admin_server_sg = Admin_SG_Construct(
            self, 'management-sg',
            vpc=vpc_admin
        )

        admin_server = ec2.Instance(
            self, 'management-server',
            vpc=vpc_admin,
            vpc_subnets=ec2.SubnetType.PUBLIC,
            security_group=admin_server_sg.sg,
            instance_type=ec2.InstanceType('t3.nano'),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
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
        
        ##################
        ### Web Server ###
        ##################

        # WebServerSG

        web_server_sg = Web_SG_Construct(
            self, 'production-sg',
            vpc=vpc_web,
            trusted_source=admin_server_sg.sg
            )

        #WebServer Role for S3 read access
        web_server_role = iam.Role(
            self, 'webserver-role',
            assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3ReadOnlyAccess')
                ],
        )

        web_server = ec2.Instance(
            self, 'web-server',
            vpc=vpc_web,
            vpc_subnets=ec2.SubnetType.PUBLIC,
            role=web_server_role,
            security_group=web_server_sg.sg,
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

        s3_bucket = S3_Construct(self, 'PostDeploymentScripts', resource_access=[web_server, admin_server])

        ##########################
        ### WebServer UserData ###
        ##########################

        # download webserver script
        script_path = web_server.user_data.add_s3_download_command(
            bucket=s3_bucket.script_bucket,
            bucket_key='launch-web-server.sh',
        )
        web_server.user_data.add_execute_file_command(file_path=script_path)

        # download website page
        web_server.user_data.add_s3_download_command(
            bucket=s3_bucket.script_bucket,
            bucket_key='index.html',
            local_file='/var/www/html/index.html'
        )
        # download ebs volume partition disk
        ebs_disk_path = web_server.user_data.add_s3_download_command(
            bucket=s3_bucket.script_bucket,
            bucket_key='mount-ebs.sh'
        )
        web_server.user_data.add_execute_file_command(file_path=ebs_disk_path)

        ###################
        ### Backup Plan ###
        ###################
        backup_plan = Backup_Construct(
            self, 'Backup-Plan',
            instances=[web_server],
        )
