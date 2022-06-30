from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ssm as ssm,

)
from constructs import Construct

class CodeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc1 = ec2.Vpc(
            self, 'VPC-Web',
            cidr='10.10.10.0/24',
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name='Public-Subnet',
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=26

                ),
                ec2.SubnetConfiguration(
                    name='Private-Subnet',
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=26
                )
            ],
            
        )
