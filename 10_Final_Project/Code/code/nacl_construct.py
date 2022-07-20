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

        # web public subnet
        vpc_web_nacl = ec2.NetworkAcl(
            self, 'NACL-Web-Public',
            vpc=vpc_web,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )

        # Add rules to NACL for Public subnet
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
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        vpc_web_nacl.add_entry(
            'HTTPS outbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )
        vpc_web_nacl.add_entry(
            'Ephemeral outbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=300,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )
        vpc_web_nacl.add_entry(
            'Ephemeral inbound allow',
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=300,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )






        ## TEMPORARY ####################################################################################
        vpc_web_nacl.add_entry(
            'SSH inbound allow',
            cidr=ec2.AclCidr.ipv4(vpc_admin.vpc_cidr_block),
            rule_number=5000,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )


        ###########################
        ### web private subnets ###
        ###########################

        vpc_web_priv_nacl = ec2.NetworkAcl(
            self, 'NACL-Web-Private',
            vpc=vpc_web,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            )
        )

        # Add rules to NACL for Private subnet
        vpc_web_priv_nacl.add_entry(
            'SSH inbound allow',
            cidr=ec2.AclCidr.ipv4(vpc_admin.vpc_cidr_block),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        vpc_web_priv_nacl.add_entry(
            'Ephemeral outbound allow',
            cidr=ec2.AclCidr.ipv4(vpc_admin.vpc_cidr_block),
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW,
        )
        vpc_web_priv_nacl.add_entry(
            'Ephemeral inbound allow',
            cidr=ec2.AclCidr.ipv4(vpc_admin.vpc_cidr_block),
            rule_number=200,
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
            'SSH outbound allow Subnet',
            cidr=ec2.AclCidr.ipv4(vpc_web.vpc_cidr_block),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )
        vpc_admin_nacl.add_entry(
            'Ephemeral inbound allow Subnet',
            cidr=ec2.AclCidr.ipv4(vpc_web.vpc_cidr_block),
            rule_number=10000,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )
        vpc_admin_nacl.add_entry(
            'Ephemeral outbound allow Subnet',
            cidr=ec2.AclCidr.ipv4(vpc_web.vpc_cidr_block),
            rule_number=10000,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )
        
        
        # Add all trusted IP addresses 
        rule_number = 500

        for ip_address in TRUSTED_IP:
            vpc_admin_nacl.add_entry(
                'SSH inbound allow AdminIP',
                cidr=ec2.AclCidr.ipv4(f'{ip_address}/32'),
                rule_number=rule_number,
                traffic=ec2.AclTraffic.tcp_port(22),
                direction=ec2.TrafficDirection.INGRESS,
                rule_action=ec2.Action.ALLOW
            )
            # vpc_admin_nacl.add_entry(
            #     'RDP inbound allow AdminIP',
            #     cidr=ec2.AclCidr.ipv4(f'{ip_address}/32'),
            #     rule_number=rule_number,
            #     traffic=ec2.AclTraffic.tcp_port(3389),
            #     direction=ec2.TrafficDirection.INGRESS,
            #     rule_action=ec2.Action.ALLOW
            # )
            # vpc_admin_nacl.add_entry(
            #     'WinRM inbound allow AdminIP',
            #     cidr=ec2.AclCidr.ipv4(f'{ip_address}/32'),
            #     rule_number=rule_number,
            #     traffic=ec2.AclTraffic.tcp_port(5985),
            #     direction=ec2.TrafficDirection.INGRESS,
            #     rule_action=ec2.Action.ALLOW
            # )
            vpc_admin_nacl.add_entry(
                'Ephemeral inbound allow AdminIP',
                cidr=ec2.AclCidr.ipv4(f'{ip_address}/32'),
                rule_number=(rule_number+100),
                traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
                direction=ec2.TrafficDirection.INGRESS,
                rule_action=ec2.Action.ALLOW
            )
            vpc_admin_nacl.add_entry(
                'Ephemeral outbound allow AdminIP',
                cidr=ec2.AclCidr.ipv4(f'{ip_address}/32'),
                rule_number=(rule_number+100),
                traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
                direction=ec2.TrafficDirection.EGRESS,
                rule_action=ec2.Action.ALLOW
            )

            rule_number += 100
