# Tech Grounds Final Project V1.0
This is version 1.0 of the final project for the Tech Grounds Cloud Engineer cohort. From our coaches, we received a document in which the specifications, requirements and a sketch were supplied. Our task was to implement it as Infrastructure as Code, make suggestions/improvements on the way and work with the Scrum methodology.

# Design

# Quick Start Guide

## Requirements
- [Python 3 installed (make sure it's added to the PATH)](https://www.python.org/)
- [AWS CLI installed](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
- [Configure your Access key + region for your AWS account](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
- [NodeJS installed (npm)](https://nodejs.org/)
- AWS CDK installed (run: `npm install -g aws-cdk`)

## Preparations
Create a virtualenv:
```
$ python -m venv .venv
```

Activate your virtualenv.

```
$ source .venv/bin/activate

or

$ . .venv/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```
## Configuration File
There are two configurable settings:
- **TRUSTED_IP** - Allow SSH access from these IP addresses. By default, your current public IP will be added. Any additional IP addresses need to be added to the list as strings: `[my_ip, "35.68.133.14", "56.175.25.219"]`
- **TEST_ENV** - When set to true, certain resources such as S3 bucket, Backup Plans & Vaults will be deleted along with the stack. If you run a **production environment**, you want to keep these resources available, so it's **highly recommended** to set this setting to False. The default setting is True, so all resources get deleted.

You can find the configuration file in the code directory, the file is named `_config.py`.  
  
[Click here for a shortcut](./code/_config.py)

Alternatively, you can run the following command to open it in VSC:
```
$ code ./code/_config.py
```

## Deploying

Now you can bootstrap your environment to your stack (this adds your account settings such as the region to the Stack)

```
$ cdk bootstrap
```

By default, the configuration has been set to TEST_MODE and your current public IP address will be used for the firewalls.  
If that is alright and you want to continue to deploy:

```
$ cdk deploy
```

## Cleaning Up

After testing the infrastructure, you can destroy the whole stack with the following command:
```
$ cdk destroy
```

If the TEST_ENV setting in the configuration file was set to True, all resources will be deleted. Else you may need to manually delete an S3 bucket, Backup Plan & Vault and the additional EBS Volume.
