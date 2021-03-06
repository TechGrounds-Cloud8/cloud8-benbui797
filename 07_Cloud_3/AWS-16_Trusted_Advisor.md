# AWS-16 Trusted Advisor
AWS Trusted Advisor provides recommendations that help you follow AWS best practices. Trusted Advisor evaluates your account by using checks. These checks identify ways to optimize your AWS infrastructure, improve security and performance, reduce costs, and monitor service quotas. You can then follow the check recommendations to optimize your services and resources.  
  
AWS Basic Support and AWS Developer Support customers can access core security checks and all checks for service quotas. AWS Business Support and AWS Enterprise Support customers can access all checks, including cost optimization, security, fault tolerance, performance, and service quotas.  
  
The Trusted Advisor can do checks in different categorys.  
  
**Cost optimization**  
Trusted Advisor can help you save cost with actionable recommendations by analyzing usage, configuration and spend. Examples include identifying idle RDS DB instances, underutilized EBS volumes, unassociated Elastic IP addresses, and excessive timeouts in Lambda functions.  
  
**Performance**  
Trusted Advisor can help improve the performance of your services with actionable recommendations by analyzing usage and configuration. Examples include analyzing EBS throughput and latency, compute usage of EC2 instances, and configurations on CloudFront.  
  
**Security**  
Trusted Advisor can help improve the security of your AWS environment by suggesting foundational security best practices curated by security experts. Examples include identifying RDS security group access risk, exposed access keys, and unnecessary S3 bucket permissions.  
  
**Fault tolerance**  
Trusted Advisor can help improve the reliability of your services. Examples include examining Auto scaling EC2 groups, deleted health checks on Route 53, disabled Availability Zones, and disabled RDS backups.  
  
**Service quotas**  
Service quotas are the maximum number of resources that you can create in an AWS account.  AWS implements quotas to provide highly available and reliable service to all customers, and protects you from unintentional spend. Trusted Advisor will notify you once you reach more than 80% of a service quota. You can then follow recommendations to delete resources or request a quota increase.  

On the basic and developer support plans, only the service quotas and 6 security checks are enabled. 
  
### Sources
- https://aws.amazon.com/premiumsupport/technology/trusted-advisor/
