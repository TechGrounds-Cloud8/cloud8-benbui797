from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct

from code._config import TRUSTED_IP


class Admin_SG_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.sg = ec2.SecurityGroup(
            self, construct_id,
            vpc=vpc,
            allow_all_outbound=False
        )

        # Allow SSH from trusted IPs
        for ip in TRUSTED_IP:
            self.sg.add_ingress_rule(
                peer=ec2.Peer.ipv4(f'{ip}/32'),
                connection=ec2.Port.tcp(22),
                description='Allow SSH access from trusted IP'
            )


class Web_SG_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc, trusted_source, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.sg = ec2.SecurityGroup(
            self, construct_id,
            vpc=vpc,
            allow_all_outbound=False
        )

        self.sg.connections.allow_from(
            other=trusted_source,
            port_range=ec2.Port.tcp(22),
            description='Allow SSH traffic from Admin Server SG'
        )
        self.sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description='Allow HTTP traffic from anywhere'
        )
        self.sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
            description='Allow HTTPS traffic from anywhere'
        )

        # Allow selected outbound traffic
        self.sg.add_egress_rule(
                peer=ec2.Peer.any_ipv4(),
                connection=ec2.Port.tcp(80),
                description='Allow HTTP out to any IP'
            )
        self.sg.add_egress_rule(
                peer=ec2.Peer.any_ipv4(),
                connection=ec2.Port.tcp(443),
                description='Allow HTTPS out to any IP'
            )