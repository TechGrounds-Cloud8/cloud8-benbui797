from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
)
from constructs import Construct

from code.nacl_construct import NACLStack
from code.s3_construct import S3_Stack

import requests

class VPCStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_ip = requests.get('https://api.ipify.org').text
        print(f'IP that will be used as trusted IP: {my_ip}')

        # Create 2 VPC's and VPC peering connection
        vpc_web = ec2.Vpc(
            self, 'VPC-Web',
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
            self, 'VPC-Admin',
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

        network_acl = NACLStack(
            self, 'NACL',
            vpc_web=vpc_web,
            vpc_admin=vpc_admin,
            my_ip=my_ip)

        ####################
        ### Admin Server ###
        ####################
        
        # AdminServerSG
        admin_server_sg = ec2.SecurityGroup(
            self, 'admin_server_sg',
            vpc=vpc_admin,
            allow_all_outbound=True
        )
        
        admin_server_sg.add_ingress_rule(
            # ec2.Peer.ipv4(f'{my_ip}/32'),
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(22),
            'Allow SSH access from trusted IP'
        )

        admin_server = ec2.Instance(
            self, 'adminserver',
            vpc=vpc_admin,
            vpc_subnets=ec2.SubnetType.PUBLIC,
            security_group=admin_server_sg,
            instance_type=ec2.InstanceType('t2.micro'),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            key_name='ec2-key-pair',
        )
        
        ##################
        ### Web Server ###
        ##################

        # WebServerSG
        web_server_sg = ec2.SecurityGroup(
            self, 'web_server_sg',
            vpc=vpc_web,
            allow_all_outbound=True
        )
        # web_server_sg.add_ingress_rule(
        #     admin_server_sg,
        #     ec2.Port.tcp(22),
        #     'Allow SSH access from anywhere'
        # )
        web_server_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            'Allow HTTP traffic from anywhere'
        )
        web_server_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(443),
            'Allow HTTPS traffic from anywhere'
        )
        web_server_sg.connections.allow_from(
            admin_server_sg,
            ec2.Port.tcp(22),
            'Allow SSH traffic from Admin Server SG'
        )

        #WebServer Role
        web_server_role = iam.Role(
            self, 'webserver-role',
            assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3ReadOnlyAccess')
                ],
        )

        web_server = ec2.Instance(
            self, 'webserver',
            vpc=vpc_web,
            vpc_subnets=ec2.SubnetType.PUBLIC,
            role=web_server_role,
            security_group=web_server_sg,
            instance_type=ec2.InstanceType('t2.micro'),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            key_name='ec2-key-pair',
        )
        
        web_server.add_user_data(
            """
            #!/bin/bash
            sudo yum update -y
            sudo yum install httpd -y
            sudo systemctl enable httpd
            sudo systemctl start httpd
            echo '<html><h1>Hello From The Web Server!</h1></html>' > /var/www/html/index.html
            """
        )

        #################
        ### S3 Bucket ###
        #################

        s3_bucket = S3_Stack(self, 'S3_Bucket', resource_access=[web_server, admin_server])
        