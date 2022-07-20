from aws_cdk import (
    aws_ec2 as ec2,
    aws_elasticloadbalancingv2 as elbv2
)
from constructs import Construct

from code._config import TRUSTED_IP

class ELB_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc, asg, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create ALB
        self.alb = elbv2.ApplicationLoadBalancer(
            self, 'ALB',
            vpc=vpc,
            internet_facing=True,
            idle_timeout=65,
            # vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        )

        # # Create Target Group
        # self.tg = elbv2.ApplicationTargetGroup(
        #     self, 'TG1',
        # )

        listener = self.alb.add_listener(
            "listener",
            # certificates=                                                                                     ######## ADD CERTIFICATE FOR HTTPS
            port=80,
            open=True,
        )

        listener.add_targets(
            'WebApp Fleet',
            port=80,
            targets=[asg]
        )