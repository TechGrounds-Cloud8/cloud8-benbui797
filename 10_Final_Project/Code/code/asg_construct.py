from aws_cdk import (
    aws_ec2 as ec2,
    aws_autoscaling as autoscaling
)

from constructs import Construct

from code._config import MIN_CAPACITY, MAX_CAPACITY, TEST_ENV

class ASG_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc_web, security_group, role, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # # AMI
        # self.custom_AMI = ec2.GenericLinuxImage(
        #     ami_map={
        #         'eu-central-1': 'ami-id'                                                ############# ADD CUSTOM AMI ID
        #     }
        # )

        user_data = ec2.UserData.for_linux()
        user_data.add_commands('sudo yum update -y && sudo yum install httpd -y && sudo systemctl start httpd && sudo systemctl enable httpd.service')
        
        # Create Launch Template
        self.launch_template = ec2.LaunchTemplate(
            self, 'Launch Template',
            launch_template_name='app-prod-launch-template',
            instance_type=ec2.InstanceType('t3.nano'),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
                ),                                                                               ########## EDIT TO CUSTOM AMI LATER!
            key_name='ec2-key-pair',
            security_group=security_group,
            role=role,
            block_devices=[
                ec2.BlockDevice(
                    device_name='/dev/xvda',
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=True,
                        delete_on_termination=TEST_ENV,
                    ))],
            user_data=user_data
        )

        # Create AutoScaling Group
        self.auto_scaling_group = autoscaling.AutoScalingGroup(
            self, 'Auto-Scaling Group',
            vpc=vpc_web,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            launch_template=self.launch_template,
            min_capacity=MIN_CAPACITY,
            max_capacity=MAX_CAPACITY,
        )

        # Configure Scaling Policy
        self.auto_scaling_group.scale_on_cpu_utilization(
            'CPU-tracking',
            target_utilization_percent=80,
        )
