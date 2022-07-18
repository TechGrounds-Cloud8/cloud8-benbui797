## Private Subnets
The max amount of servers the ASG can scale to is 3, but in order to design for high availability, we'll create 3 private subnets so every server will be launched in a different AZ.

## EFS file system
It is a best practise to seperate the root disk and data disk, but when we use auto-scaling, EFS is easier to accomplish this than EBS. 