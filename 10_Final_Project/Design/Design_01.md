# Design

## VPC / Network
- There are two VPC's (10.10.10.0/24 and 10.20.20.0/24)
- Both VPC's have a private and public subnet
- The VPC's have a Peering connection
- The Subnets need to be protected on a Subnet level (NACL)

## Instances / SG
- Two EC2 instances; Web Server and Management Server (they should be in different VPCs)
- The webserver should automatically install (User Data)
- WebServer: HTTP(S): port 80/443 / SSH: port 22
- WebServer: SSH connections via the Admin server IP only (Bastion Host)
- AdminServer: SSH port 22
- AdminServer: SSH connections only via trusted IP's (office/admin)
- All instances should have encrypted storage

## Storage / Backup
- WebServer must make a daily backup
- Backup must be stored for 7 days (lifecycle management)
- AWS Backup: Backup plan?
- S3 bucket that contains the bash scripts for launch.

## Assumptions:
- Requirements don't say that the WebServer needs to be accessable from the internet. In the diagram, it is in the public subnet, which means it has a public IP.
- IAM policy? EC2 Keys?
- Automated Security Responses? (AWS Solutions library)
- Can I export Stack to Diagram.io for drawing?

## Suggestions
- Check Security Hub (Security Score) after network is up? Add security tips to documentation/recommendations?

## Unknowns:
- Which regions?
- Instance requirements? Resources?
- What are the trusted IP addresses?

- S3 with PostDeploymentScripts?

### Product Owner questions:
- AdminServer office IP SSH - SSM is best practise?


## Sources:
- [CDK Workshop](https://cdkworkshop.com/30-python.html)
- [CDK Documentation](https://docs.aws.amazon.com/cdk/v2/guide/home.html)
- [CDK API Documentation](https://docs.aws.amazon.com/cdk/api/v2/)
- [Create a custom VPC with AWS CDK](https://levelup.gitconnected.com/creating-a-custom-vpc-with-aws-cdk-52f8788cb2d5)
- [EC2 Instance Connect (BASTION HOST SSH ALTERNATIVE)](https://aws.amazon.com/de/blogs/compute/new-using-amazon-ec2-instance-connect-for-ssh-access-to-your-ec2-instances/)
- [info about linux /dev/null (using exitcode in bash scripts)](https://linuxhint.com/what_is_dev_null/)

- https://dev.to/aws-builders/ping-me-part-1-vpc-peering-using-cdk-2kpd
- https://bobbyhadz.com/blog/aws-cdk-ec2-instance-example
- Add NACL rules when using LoadBalancer: https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html#elb-vpc-nacl
- https://aws.amazon.com/blogs/storage/automate-data-recovery-validation-with-aws-backup/


- https://stackoverflow.com/questions/26873289/how-to-check-a-disk-for-partitions-for-use-in-a-script-in-linux
- https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs
- https://linuxhint.com/what_is_dev_null/