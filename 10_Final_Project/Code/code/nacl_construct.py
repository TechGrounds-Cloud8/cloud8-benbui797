from aws_cdk import (
    aws_ec2 as ec2,
)
from constructs import Construct

from code._config import TRUSTED_IP


class NACL_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc_web, vpc_admin, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ######################################
        ### Create Network ACL for VPC Web ###
        ######################################

        vpc_web_nacl = ec2.NetworkAcl(
            self, 'VPC-1 Web',
            vpc=vpc_web,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )

        # Add rules to NACL
        vpc_web_nacl.add_entry(
            'HTTP inbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        vpc_web_nacl.add_entry(
            'HTTP outbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )
        vpc_web_nacl.add_entry(
            'HTTPS inbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        vpc_web_nacl.add_entry(
            'HTTPS outbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )
        vpc_web_nacl.add_entry(
            'SSH inbound allow',
            cidr=ec2.AclCidr.ipv4(vpc_admin.vpc_cidr_block),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        vpc_web_nacl.add_entry(
            'Ephemeral outbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )
        vpc_web_nacl.add_entry(
            'Ephemeral inbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=130,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        ########################################
        ### Create Network ACL for VPC Admin ###
        ########################################

        vpc_admin_nacl = ec2.NetworkAcl(
            self, 'VPC-Admin NACL',
            vpc=vpc_admin,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )

        # Add rules to NACL
        vpc_admin_nacl.add_entry(
            'SSH inbound allow Subnet',
            cidr=ec2.AclCidr.ipv4(vpc_web.vpc_cidr_block),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        vpc_admin_nacl.add_entry(
            'SSH outbound allow Subnet',
            cidr=ec2.AclCidr.ipv4(vpc_web.vpc_cidr_block),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )
        
        # Add all trusted IP addresses 
        for ip_address in TRUSTED_IP:
            vpc_admin_nacl.add_entry(
                'SSH inbound allow AdminIP',
                cidr=ec2.AclCidr.ipv4(f'{ip_address}/32'),
                rule_number=100,
                traffic=ec2.AclTraffic.tcp_port(22),
                direction=ec2.TrafficDirection.INGRESS,
                rule_action=ec2.Action.ALLOW

            )
            vpc_admin_nacl.add_entry(
                'Ephemeral outbound allow AdminIP',
                cidr=ec2.AclCidr.ipv4(f'{ip_address}/32'),
                rule_number=100,
                traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
                direction=ec2.TrafficDirection.EGRESS,
                rule_action=ec2.Action.ALLOW
            )
