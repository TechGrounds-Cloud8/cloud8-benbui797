from aws_cdk import (
    Duration,
    aws_elasticloadbalancingv2 as elbv2,
    aws_certificatemanager as acm
)
from constructs import Construct

from code._config import CERTIFICATE_ARN

class ELB_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc, asg, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create ALB
        self.alb = elbv2.ApplicationLoadBalancer(
            self, 'ALB',
            vpc=vpc,
            internet_facing=True,
            # idle_timeout=65,
            # vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        )

        # Redirect HTTP to HTTPS
        self.alb.add_redirect()

        # Import SSL Certificate
        certificate = acm.Certificate.from_certificate_arn(
            self, 'Certificate',
            certificate_arn=CERTIFICATE_ARN
            )

        # Add listener to ALB
        listener = self.alb.add_listener(
            "listener",
            port=443,
            open=True,
            certificates=[certificate],
            ssl_policy=elbv2.SslPolicy.FORWARD_SECRECY_TLS12,
        )

        # Add Target Group to Listener
        target_group = listener.add_targets(
            'WebApp Fleet',
            port=80,
            targets=[asg],            
            stickiness_cookie_duration=Duration.minutes(5),
            health_check=elbv2.HealthCheck(
                enabled=True,
                port='80'
            )
        )
