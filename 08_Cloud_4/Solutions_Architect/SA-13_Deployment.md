# Deployment and Management
## CloudFormation
- CloudFormation is the tool to use to work with *Infrastructure As Code (IAC)*.  
- Infrastructure patterns are defined in a *template* file. 
- The files can be either JSON or YAML.
- You upload the template to CloudFormation, which then builds the infrastructure according to the template.
- Benefits: 
  - Infrastructure is provisioned consistently (you create 1 template file and reuse it), so there is less chance for mistakes (human errors)
  - Less time and effort than configuring resource manually (through the console or CLI, clicking/typing the same things repeatedly)
  - Version control and peer review for your CloudFormation templates
  - Free to use (you don't pay for CloudFormation, only for the resources that are provisioned)
  - Can be used to manage updates and dependencies
  - Can be used to rollback and delete the entire stack as well
  
**Key components**
- **Templates** - The JSON or YAML text file that contains the instructions for building out the AWS environment.
- **Stacks** - The entire environment described by the template and created, updated and deleted as a single unit.
- **StackSets** - Extends the functionality of Stacks by enabling you to create, update and delete stacks across multiple accounts and regions with a single operation.
- **Change Sets** - A summary of proposed changes to your Stack that will allow you to see how those changes might impact your existing resources before implementing them.
  
## AWS Elastic Beanstalk
**Components of a Beanstalk application:**
A EB App can consist of multiple **Layers**:
- Application:
  - Contain environments, environment configurations and application versions
  - You can have multiple application versions held within an application
  - **Application Version:** A specific reference to a section of deployable code. You can revert back to a previous version. Versions are typically stored on S3.
- Environments (Development/Production):
  - An application version that has been deployed on AWS resources
  - The resources are configured and provisioned by Elastic Beanstalk.
  - **Web Servers** are standard applications that listen for and then processes HTTP requests, typically over port 80.
  - **Workers** are specialized applications that have a background processing task that listens for messages on an SQS queue. Workers should be used for long-running tasks.

## System Manager
Manages many AWS resources including EC2, S3 and RDS.
You can create documents (rules) and pass them to various components that will then perform some task.
Components are:
- **Automation** (i.e. make a snapshot of an RDS instance)
- **Run Command** (i.e. check EC2 instance for missing updates)
- **Inventory** (all kinds of data about the services, such as OS, installed applications, server roles)
- **Patch Manager** (deploy OS and software patches automatically across large groups of EC2 or on-premise instances)
- **Session Manager** (Secure remote management of your instances at scale without logging into your server (no SSH or PowerShell, so you don't need to open those ports))
   
**Parameter Store**  
- Provides secure, *hierarchical* storage for configuration data management and secrets management
- Highly scalable, available and durable
- Store data such as passwords, database strings and license codes as parameter values
- You can values as plaintext or ciphertext (encrypted)
- You can reference parameters in your scripts, commands, SSM documents, and configuration and automation workflows by using the unique name that you specified when you created the parameter
- No native rotation of keys (difference with AWS Secrets Manager, which does it automatically) - but you could write a lambda function.
- Key/Value Type: 
  - String
  - StringList
  - SecureString (optional encryption with KMS)
- Free for standard (up to a certain volume), charges for advanced

## AWS Secrets Manager
- Secrets Manager stores and rotates secrets (passwords, credentials etc) safely without the need for code deployments.  
- Secrets Manager offers automatic rotation of credentials (built-in) for:
  - AWS RDS (MySQL, PortgreSQL and Aurora)
  - AWS RedShift
  - AWS DocumentDB
- For services not in that list, you can write your own Lambda functions for automatic rotation.
- Key/Value Type: 
  - String
  - Binary (always encrypted with KMS)
- Charges apply per secret

## AWS OpsWorks
OpsWorks is a configuration management service that provides managed instances of *Chef* and *Puppet*.  
  
The updates managed by OpsWorks include:
- patching
- updating
- backup
- configuration
- compliance management
  
Similar to AWS Systems Manager, but used for customers who already use Chef/Puppet.

## AWS Resource Access Manager (RAM)
AWS RAM lets you share resources:
  - Across AWS accounts
  - Within Organisations or OUs
  - IAM roles and IAM users
  
Resource shares are created with:
  - AWS RAM console
  - AWS RAM API
  - AWS CLI
  - AWS SDK
  
RAM can be used to share:
- AWS App Mesh
- Amazon Aurora
- AWS Certificate Manager Private Certificate Authority
- AWS CodeBuild
- Amazon EC2
- EC2 Image Builder
- AWS Glue
- AWS License Manager
- AWS Network Firewall
- AWS Outposts
- Amazon S3 on Outposts
- AWS Resource Groups
- Amazon Route 53
- AWS Systems Manager Incident Manager
- Amazon VPC
  
https://docs.aws.amazon.com/ram/latest/userguide/shareable.html

