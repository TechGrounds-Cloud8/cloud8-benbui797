#!/usr/bin/env python3
import os

import aws_cdk as cdk

from code.iac_stack import IACStack

env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))

app = cdk.App()

IACStack(app, "TG-FP-V1",
    env=env
    # env=cdk.Environment(account='880133342642', region='eu-central-1'),
    )

app.synth()
