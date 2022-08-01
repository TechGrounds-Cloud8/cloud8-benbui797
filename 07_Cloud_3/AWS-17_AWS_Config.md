# AWS-17 AWS Config
AWS Config provides a detailed view of the configuration of the supported resources in your account, you can make backups of them, or use them to audit your account.  
Auditing basically functions like a filter based on configuration parameters, for example, show all resources that belong a security group or are unencrypted. You can create a Config Rule which is more or less a blueprint for your ideal configuration. AWS Config then compares your current setup to the Rule and gives you feedback regarding any resources that don't comply. 
  
With AWS Config, you can do the following:
- Evaluate your AWS resource configurations for desired settings.
- Get a snapshot of the current configurations of the supported resources that are associated with your AWS account.
- Retrieve configurations of one or more resources that exist in your account.
- Retrieve historical configurations of one or more resources.
- Receive a notification whenever a resource is created, modified, or deleted.
- View relationships between resources. For example, you might want to find all resources that use a particular security group.
  
This can be very useful to make sure your account is up to the standard you have defined in your rule. You can use this for:  
- **Resource Administration** - It can help you spot resources that have an error in their configurations
- **Auditing and Compliance** - In some sectors, you may be required to provide historical configurations for auditing purposes.
- **Managing and Troubleshoot Configuration Changes** - Having an overview and a backup of your configurations can help you access the relationship between resources and help you troubleshoot any issues that might occur after a change.
- **Security Analysis** Config can also help you analyse security weaknesses. You may need to look back in time at your IAM settings, whether a certain account had permission to do something or a certain port was open at that time.

## Key terminology
- **Configuration Recorder** The configuration recorder stores the configurations of the supported resources in your account as configuration items. You must first create and then start the configuration recorder before you can start recording. You can stop and restart the configuration recorder at any time.
- **Configuration Snapshot** A configuration snapshot is a collection of the configuration items for the supported resources that exist in your account. This configuration snapshot is a complete picture of the resources that are being recorded and their configurations.
- **Configuration Stream** A configuration stream is an automatically updated list of all configuration items for the resources that AWS Config is recording. Every time a resource is created, modified, or deleted, AWS Config creates a configuration item and adds to the configuration stream.

## Exercise
### Sources
- https://aws.amazon.com/config/
- https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html
