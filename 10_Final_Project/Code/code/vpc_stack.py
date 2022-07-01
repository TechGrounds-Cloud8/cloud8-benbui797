from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ssm as ssm,

)
from constructs import Construct

class VPCStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

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
                ec2.SubnetConfiguration(
                    name='Private',
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=26
                )],
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

        ec2.CfnVPCPeeringConnection(
            self, 'peer_vpc_id',
            peer_vpc_id=vpc2.vpc_id,
            vpc_id=vpc1.vpc_id,
        ) 

    
