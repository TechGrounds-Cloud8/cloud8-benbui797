from aws_cdk import (
    # aws_s3_deployment as s3_deploy
    aws_s3 as s3
)
from constructs import Construct

class S3_Stack(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.script_bucket = s3.Bucket(
            self, 'Script Bucket',
                        
        )