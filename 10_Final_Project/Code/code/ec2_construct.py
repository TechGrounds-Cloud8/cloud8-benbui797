from aws_cdk import (
    aws_ec2 as ec2,
)
from constructs import Construct

from code._config import TRUSTED_IP

class EC2_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc_web, vpc_admin, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        