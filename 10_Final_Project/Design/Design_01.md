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

## Assumptions:
- Requirements don't say that the WebServer needs to be accessable from the internet. In the diagram, it is in the public subnet, which means it has a public IP.
- IAM policy? EC2 Keys?
- Automated Security Responses? (AWS Solutions library)
- Check Security Hub (Security Score) after network is up
- Can I export Stack to Diagram.io for drawing?

## Suggestions
- 

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