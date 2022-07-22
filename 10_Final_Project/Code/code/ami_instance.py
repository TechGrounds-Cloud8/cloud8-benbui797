from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct

from code._config import TEST_ENV

class AMI_Construct(Construct):

    def __init__(self, scope: Construct, construct_id: str, vpc, security_group, role, s3_bucket, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.ami_instance = ec2.Instance(
            self, 'web-server',
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            role=role,
            security_group=security_group,
            instance_type=ec2.InstanceType('t3.nano'),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
                ),
            key_name='ec2-key-pair',
            block_devices=[
                ec2.BlockDevice(
                    device_name='/dev/xvda',
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=True,
                        delete_on_termination=TEST_ENV,
                    ))]
        )

        ##########################
        ### WebServer UserData ###
        ##########################

        # download webserver script
        script_path = self.ami_instance.user_data.add_s3_download_command(
            bucket=s3_bucket.script_bucket,
            bucket_key='launch-web-server.sh',
        )
        self.ami_instance.user_data.add_execute_file_command(file_path=script_path)

        # download website content
        self.ami_instance.user_data.add_s3_download_command(
            bucket=s3_bucket.script_bucket,
            bucket_key='website_content.zip',
            local_file='/tmp/website_content.zip'
        )
        # unzip website content
        self.ami_instance.user_data.add_commands("chmod 755 -R /var/www/html/")
        self.ami_instance.user_data.add_commands("unzip /tmp/website_content.zip -d /var/www/html/")
