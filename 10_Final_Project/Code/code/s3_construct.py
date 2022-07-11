from aws_cdk import (
    Duration,
    RemovalPolicy,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_iam as iam,
)
from constructs import Construct

import os

path = os.getcwd()

class S3_Stack(Construct):

    def __init__(self, scope: Construct, construct_id: str, resource_access, test: bool, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        if test:
            auto_removal = RemovalPolicy.DESTROY
        else:
            auto_removal = RemovalPolicy.RETAIN

        self.script_bucket = s3.Bucket(
            self, 'Script Bucket',
            encryption=s3.BucketEncryption.S3_MANAGED,
            versioned=True,
            enforce_ssl=True,
            intelligent_tiering_configurations=[s3.IntelligentTieringConfiguration(
                name='Intelligent-Tiering',
                archive_access_tier_time=Duration.days(90),
                deep_archive_access_tier_time=Duration.days(180),
            )],
            removal_policy=auto_removal,
            auto_delete_objects=test,
        )

        self.deployment = s3deploy.BucketDeployment(
            self, 'Bucket Deployment',
            destination_bucket=self.script_bucket,
            sources=[s3deploy.Source.asset(os.path.join(path, "assets"))]
            )
        
        self.script_bucket.add_to_resource_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                principals=[iam.ServicePrincipal('ec2.amazonaws.com')],
                actions=['s3:GetObject'],
                resources=[f'{self.script_bucket.bucket_arn}/*'])
        )
