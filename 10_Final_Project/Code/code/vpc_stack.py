from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ssm as ssm,
)
from constructs import Construct

class VPCStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create 2 VPC's and VPC peering connection
        vpc1 = ec2.Vpc(
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

        vpc2 = ec2.Vpc(
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
            peer_vpc_id=vpc2.vpc_id,
            vpc_id=vpc1.vpc_id,
        ) 

        # Update Route Tables for Peering Connection

        for subnet in vpc1.public_subnets:
            route_table_entry = ec2.CfnRoute(
                self, 'VPC-1 Peer Route',
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block='10.10.20.0/24',
                vpc_peering_connection_id=vpc_peer.ref,
            )

        for subnet in vpc2.public_subnets:
            route_table_entry = ec2.CfnRoute(
                self, 'VPC-2 Peer Route',
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block='10.10.10.0/24',
                vpc_peering_connection_id=vpc_peer.ref,
            )
