## CIDR blocks
In V1.0 the request was to use /24 for the VPC's, but why not use /16? There are no disadvantages, but it makes management far easier and allows for a lot of room for growth!


name= app-prd-vpc
cidr= 10.10.0.0/16

name= management-prd-vpc
cidr= 10.20.0.0/16

The subnets will use /24.

## Private Subnets
The max amount of servers the ASG can scale to is 3, but in order to design for high availability, we'll create 3 private subnets so every server will be launched in a different AZ. This only applies to the "app-prd-vpc". The management vpc doesn't require private subnets, so will remain unchanged.

## EFS file system
It is a best practise to seperate the root disk and data disk, but when we use auto-scaling, EFS is easier to accomplish this than EBS. 

## Environment
[It's recommended for production stacks to explicitly specify the environment for the stack in the .app file.](https://docs.aws.amazon.com/cdk/v2/guide/environments.html)

## Certificate
Import certificate in ACM and ARN to certificate to Parameter store

# Parameter Store
- Add Office IP to parameter store
- Add AMI id to parameter store
- Add ARN to Certificate to parameter store

## SSL offloading
Encryption and decryption require a bit of computing power, so in order to speed up traffic over the internal network, we allow for SSL offloading at the ALB.

## Backup
The backups get made of the EFS filesystem instead of single EC2 instances