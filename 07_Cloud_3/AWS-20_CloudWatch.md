# AWS-20 CloudWatch
CloudWatch collects monitoring and operational data in the form of logs, metrics, and events, and visualizes it using automated dashboards so you can get a unified view of your AWS resources, applications, and services that run in AWS and on-premises. You can correlate your metrics and logs to better understand the health and performance of your resources. You can also create alarms based on metric value thresholds you specify, or that can watch for anomalous metric behavior based on machine learning algorithms. To take action quickly, you can set up automated actions to notify you if an alarm is triggered and automatically start auto scaling, for example, to help reduce mean-time-to-resolution. You can also dive deep and analyze your metrics, logs, and traces, to better understand how to improve application performance.
  
![AWS-20 1](../00_includes/CLOUD03/AWS-20_1.png)  
  
It is integrated to a lot of services within AWS, for examply, during the assignment where we set up a Load Balancer with Auto-Scaling, it received the CPU metric from CloudWatch. This is an automated response to an *Event*.  
  
You can also set up an alarm that will notify you via SNS (Simple Notification Service).



## Key terminology
- **AWS-X-Ray** Another logging service, but this time specifically about the requests your applications receive and also the requests they send out to other resources. It can be useful to identify bottlenecks that cause performance issues.  

## Exercise
### Sources
- https://aws.amazon.com/cloudwatch/
- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html
- https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html

### Overcome challenges
- N/A

### Results
Here is an example of a dashboard for EC2 instances in CloudWatch. Currently I don't have any instances running, so you don't see any metrics, but we have already shown this in a couple of previous exercises.   
![AWS-20 2](../00_includes/CLOUD03/AWS-20_2.png)  
  
In the alarm screen there is an huge amount of options. You can select metrics from the menu (for EC2 instances there are already 255 options!). On top of that you can add functions (sum, average etc) and other queries. 
![AWS-20 3](../00_includes/CLOUD03/AWS-20_3.png)  
  
In the next screen you can select a treshhold value or a band (so there is a greater acceptable area). You can also create different alarms for different conditional options (<, <=, >=, >). And you can add a required amount of metric breaches before your alarm actually activates.  
  
Then you can add Alarm actions, for example, reboot an instance or use an SNS topic, or create a new topic.