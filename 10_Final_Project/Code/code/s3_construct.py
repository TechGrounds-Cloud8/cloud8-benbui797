from aws_cdk import (
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
)
from constructs import Construct

import os

path = os.getcwd()

class S3_Stack(Construct):

    def __init__(self, scope: Construct, construct_id: str, resource_access, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.script_bucket = s3.Bucket(
            self, 'Script Bucket',
            encryption=s3.BucketEncryption.S3_MANAGED,
            versioned=True,
            # public_read_access=True,
        )

        for principal in resource_access:
            # self.script_bucket.add_to_resource_policy(principal)
            self.script_bucket.grant_read(principal)

        self.deployment = s3deploy.BucketDeployment(
            self, 'Bucket Deployment',
            destination_bucket=self.script_bucket,
            sources=[s3deploy.Source.asset(os.path.join(path, "assets"))]
            )
        
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_s3_assets/README.html
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_s3_deployment/README.html
