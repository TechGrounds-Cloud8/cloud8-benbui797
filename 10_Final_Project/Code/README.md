# Tech Grounds Final Project V1.0
This is version 1.0 of the final project for the Tech Grounds Cloud Engineer cohort. From our coaches, we received a document in which the specifications, requirements and a sketch were supplied. Our task was to implement it as Infrastructure as Code, make suggestions/improvements on the way and work with the Scrum methodology.

# Design

# Quick Start Guide

## Requirements
- Python 3 installed
- NodeJS installed (npm)
- AWS CLI installed
- AWS CDK installed

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

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```



## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation


