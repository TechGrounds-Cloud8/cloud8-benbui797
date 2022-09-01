from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    Stack
)
from constructs import Construct

from code._config import TRUSTED_IP

class WEB_VPC_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc_web = ec2.Vpc(
            self, 'app-prd-vpc',
            cidr='10.10.0.0/16',
            nat_gateways=0,
            max_azs=2,
            enable_dns_hostnames=True,
            enable_dns_support=True,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name='Public',
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                ),                
                ec2.SubnetConfiguration(
                    name='Private',
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=24
                )],
            gateway_endpoints={
                'S3': ec2.GatewayVpcEndpointOptions(
                    service=ec2.GatewayVpcEndpointAwsService.S3
                )
            }
        )
        
        self.vpc_web.add_interface_endpoint("ec2messages", service=ec2.InterfaceVpcEndpointAwsService.EC2_MESSAGES)
        self.vpc_web.add_interface_endpoint("ssm", service=ec2.InterfaceVpcEndpointAwsService.SSM)
        self.vpc_web.add_interface_endpoint("ssmmessages", service=ec2.InterfaceVpcEndpointAwsService.SSM_MESSAGES)
        

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