from aws_cdk import (
    aws_ec2 as ec2,
)
from constructs import Construct

from code._config import TRUSTED_IP, AVAILABILITY_ZONES

class WEB_VPC_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc_web = ec2.Vpc(
            self, 'app-prd-vpc',
            cidr='10.10.0.0/16',
            nat_gateways=0,
            max_azs=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name='Public',
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                )]
        )

        # Add private subnets to VPC
        private_network_number = 1
        for az in AVAILABILITY_ZONES:
            private_subnets = ec2.PrivateSubnet(
                self, f'{az}-private-subnet',
                vpc_id=self.vpc_web.vpc_id,
                cidr_block=f'10.10.{private_network_number}.0/24',
                availability_zone=az                
            )
            private_network_number += 1



class ADMIN_VPC_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc_admin = ec2.Vpc(
            self, 'management-prd-vpc',
            cidr='10.20.0.0/16',
            max_azs=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name='Public',
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                )]
            )