# CloudTrail
- CloudTrail logs API activity for auditing (every button in the console or command in the AWS CLI is an API call)
- By default, management events are logged and retained for 90 days
- A **CloudTrail Trail** logs any events to S3 for indefinite retention
  - If you have AWS Organisations enabled, you can enable a Trail across accounts
- Trail can be within Region or all Regions
- CloudWatch Events can triggered based on API calls in CloudTrail
- Events can be streamed to CloudWatch Logs (typically go to S3, but can be send to Logs as well)
  
**log file integrity validation**  
It checks whether the logged events have been tempered with. Because this data is used for auditing and compliance, we need to be sure this information is accurate and has not been modified.

## Type of Events
- **Management Events** - information about management operations that are performed on the resources in your AWS account (launch/terminate an EC2 instance). Logs Who/What/When performed that action
- **Data events** - information about resource operations performed on or in a resource (for example, actions within S3)
- **Insight events** - identify and respond to unusual activity associated with write API calls by continuously analyzing CloudTrail management events.