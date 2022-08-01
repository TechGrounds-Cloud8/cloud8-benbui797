# AWS-E1 CLI
Doing exercises AWS-05, 06, 07 again, but then using the AWS CLI interface.

## Key terminology
- **AWS CloudShell** browser-based CLI tool
- `aws <command> <subcommand> [options and parameters]` syntax for using AWS CLI
- `aws <command> wait <subcommand> [options and parameters]` using the wait command, the API waits until current call is complete before moving to next command. command = service, subcommand = action. 
- `--option key1=value1,key2=value2,key3=value3` shorthand for multiple parameters&values (for Linux and MacOS). Add quotes for Windows/Powershell
- **auto-prompt** allows you to enter a partial command (or just a letter). A list with available options is shown and you can use arrow keys + SPACE to select the command, followed by ENTER. Or F3 for documentation.
  
**S3 commands**  
- `aws s3 mb s3://<bucketname> --options` mb = make bucket. options can be: `--region <region>`
- mv/cp/sync for file operations
- `aws s3 presign s3://<bucketname/file> --expires-in <seconds>` generate an url for that file with public access.

## Exercise
### Sources
- https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html
- https://docs.aws.amazon.com/cloudshell/latest/userguide/working-with-cloudshell.html
- https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html
- https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html#cli-aws-s3
- https://www.thegeekstuff.com/2019/04/aws-s3-cli-examples/
- https://www.thegeekstuff.com/2016/04/aws-ec2-cli-examples/

### Overcome challenges
- Reading the documentation to understand the syntax of AWS CLI.
- put-bucket-policy : invalid JSON - was not able to find the solution. 

### Results
**Creating S3 bucket with CLI tool**
