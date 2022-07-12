from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct

from code._config import TRUSTED_IP

class SG_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc,  **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.sg = ec2.SecurityGroup(
            self, construct_id,
            vpc=vpc

        )