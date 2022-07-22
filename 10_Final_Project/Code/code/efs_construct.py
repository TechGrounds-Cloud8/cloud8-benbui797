from aws_cdk import (
    RemovalPolicy,
    aws_ec2 as ec2,
    aws_efs as efs
)

from constructs import Construct

from code._config import TEST_ENV

class EFS_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        if TEST_ENV:
            auto_removal = RemovalPolicy.DESTROY
        else:
            auto_removal = RemovalPolicy.RETAIN

        self.efs = efs.FileSystem(
            self, 'EFS File System',
            vpc=vpc,
            enable_automatic_backups=True,
            encrypted=True,
            lifecycle_policy=efs.LifecyclePolicy.AFTER_14_DAYS,
            out_of_infrequent_access_policy=efs.OutOfInfrequentAccessPolicy.AFTER_1_ACCESS,
            removal_policy=auto_removal,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED)
        )