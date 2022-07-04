# Serverless
## AWS Lambda
**Primary use cases for Lambda:**
- Data processing
- Real-time file processing
- Real-time stream processing
- Build serverless backends for web, mobile, IOT and 3rd party API requests

Max runtime is 15 minutes (900 seconds)!  

### Lambda Function Invocations
**Synchronous:**
- You wait for the function to process the event and return a response
- CLI, SDK, API Gateway
- Results returned immediately
- Error handling happens on the client side (retries, exponential backoff (increase the wait time between every retry))
  
**Asynchronous:**
- Lambda queues the event for processing and returns a response immediately.
- S3, SNS, EventBridge (+ other services)
- Lambda retries up to 3 times
- Processing must be idempotent (if you keep retrying, the same result should occur)
- There is a succesful-event destination and a failed-event destination (or alternatively a Dead-letter queue, where failed events are stored for further processing)
  
**Event source mapping (stream):** 
- An event source mapping is a Lambda resource that reads from an event source and invokes a Lambda function. You can use event source mappings to process items from a stream or queue in services that don't invoke Lambda functions directly. If it's not a stream-based service, the event source is mapped on the service (i.e. API GW)
- SQS, Kinesis Data Streams, DynamoDB Streams, Amazon MQ, Amazon MSK, Apache Kafka (The event source mapping for these services can be specified on the Lambda side!)
- Lambda does the polling (polls the source)
- Records are processed in order (except for SQS standard)

### Lambda Function Concurrency
Concurrency means multiple computations are happening at the same time. It can happen on different levels:
- Multiple computers in a network
- Multiple applications running on one computer
- Multiple processors in a computer (today, processors often have mutiple cores on a single chip)
  
Concurrency is essential in modern programming:
- Web sites must handle multiple simultaneous users
- Mobile apps need to do some of their processing on servers (in the cloud)
- GUI always require background work that does not interrupt the user

[SOURCE: MIT](https://web.mit.edu/6.005/www/fa14/classes/17-concurrency/#:~:text=Concurrency%20means%20multiple%20computations%20are,cores%20on%20a%20single%20chip)  
  
When a Lambda function is repeatedly invoked, there is a queue of functions. However, they will not wait for one function to finish, instead there will be many functions running in parallel. Up to the *Burst or Account Limit*.
  
**Burst Concurrency Quotas:**   
- 3000 - US West (Oregon), US East (N. Virginia), Europe (Ireland)
- 1000 - Asia Pacific (Tokyo), Europe (Frankfurt), US East (Ohio)
- 500 - Other Regions
  
If the limit for concurrency is exceeded, throttling occurs with error message "Rate Exceeded" and 429 "TooManyRequestsException".  
NOTE! Burst Concurrency is not per function, it applies to all your functions within the Region!  
  
## Application Integration Services overview
Service | What It Does | Example Use Cases
---|---|---
Simple Queue Service | Messaging queue; store and forward patterns | Building distributed / decoupled apps
Simple Notification Service | Set up, operate and send notifications from the cloud | Send email notification when CloudWatch alarm is triggered
Step Functions | Out-of-the-box coordination of AWS service components with visual workflow | Order processing workflow
Simple Workflow Service | Need to support external processes or specialized execution logic | Human-enabled workflows like an order fulfilment system  or for procedural requests
Amazon MQ | Message broker service for Apache Active MQ and RabbitMQ | Need a message queue that supports industry standard APIs and protocols, migrate queues to AWS
Amazon Kinesis | Collect, process and analyze streaming data | Collect data from IoT devices for later processing
  
- AmazonMQ has similar functionality as AWS SQS, but supports Apache apps. 
- For newer apps, AWS recommends to use Step Functions instead of Simple Workflow Service.
  
Amazon Kinesis | Amazon SQS | Amazon SNS
---|---|---
Consumers pull data | Consumers pull data | Push data to many subscribers
As many consumers as you need | Data is deleted after being consumed | Publisher/Subscriber model
Routes related records to same record processor | Can have as many workers (consumers) as you need | Integrates with SQS for fan-out architecture pattern
Multiple applications can access stream concurrently | No ordering guarantee (except with FIFO queues) | Up to 10.000.000 subscribers
Ordering at the shard level | Provides messaging semantics | Up to 100.000 topics
Can consume records in the correct order at later time | Individual message delay | Data is not persistant
Must provision throughput | Dynamically scales | No need to provision throughput

## SQS
- **Direct integration** - A Web Tier (ASG) directly connects to an App Tier (ASG). If the App Tier cannot keep up with the workload, you'll lose data.
- **Decoupled integration** - The messages are stored in a queue (SQS). The App Tier polls the queue for new work, so it can work at it's own pace. When the Web Tier produces more messages, they just get stored in the queue.

### SQS Queue types
- **Standard Queue** 
  - **Unlimited Throughput** - Standard queues support a nearly unlimited number of transactions per second (TPS) per API action
  - **Best-effort Ordering** - Occasionally, messages might be delivered in a different order from which they were sent
  - **At-Least-Once Delivery** - A message is delivered at least once, but occasionally more than one copy of a message is delivered
- **FIFO queue**
  - **High Throughput** - FIFO queues support up to 300 messages per second (300 send, receive or delete operations per second). When you batch 10 messages per operation (maximum), FIFO queues can support up to 3000 messages per second.
  - **First-in, First-out delivery** - The first message that is placed in the queue, will be the first message that gets processed when a worker polls the queue. The order is strictly preserved.
  - **Exactly-Once Processing** - A message is delivered once and remains available until a consumer processes and deletes it. Duplicates are not introduced into the queue.
  

FIFO queues requirements:
- **Message Group ID:** The tag that specifies that a message belongs to a specific message group. Messages belonging to that group are guaranteed to be processed in a FIFO manner.
- **Message Deduplication ID:** The token used deduplicated of messages within the deduplication interval. (Exactly Once processing)
  
**SQS Dead Letter Queue**
Another queue parallel to the main queue. Any messages that fail to be processed, can be sent to the DL Queue, where they are stored. Here you can analyze why their processing didn't succeed.  
It's not a different queue type, it's either a standard or FIFO queue, but it has been specified as the Dead Letter Queue in the configuration of another queue.  
*The queue type of the sending queue and the dead-letter queue must be the same!! So both standard or both FIFO!!*  
  
**Delay Queue**
After a consumer has received the message from the queue, the message is invisible for the timeout delay (*Default Visibility Timeout*, after this time has passed, the message is visible and can be polled. Default is 30 seconds, maximum is 12 hours.  
  
In the case a consumer is not able to process the message, another consumer can try again, but by making the message invisible, its prevented that multiple consumers are processing the same message.

  
**Long Polling vs Short Polling**
- **Short Polling** The consumer will check a subset of servers and may not return all of the messages
- **Long Polling** Waits for the *WaitTimeSeconds*, which eliminates empty responses. Can reduce the amount of API calls to the queue and reduce the cost. Receive Message Wait Time is off with 0 seconds, max time is 20 seconds.

## SNS
[AWS SNS](../../07_Cloud_3/AWS-23_SNS_SQS_Event_Bridge_.md)

## Step Functions
- AWS Step Functions is used to build distributed applications as a series of steps in a visual workflow.
- You can quickly build and run *state machines* to execute the steps of your application
  1. Define the steps of your workflow in the *JSON-based Amazon States Language*. The visual console automatically graphs each step in the order of execution.
  2. Start an execution to visualize and verify the steps of your application are operating as intended. The console highlights the real-time status of each step and provides a detailed history of each execution.
  3. AWS Step Functions operates and scales the steps fo your applciation and underlying compute for you to help ensure your application executes reliably under increasing demand.

## API Gateway
Act as endpoint in your account to your resource by using RESTful APIs. You can import Swagger / Open API 3.0 definitions (YAML/JSON).

**Deployment types:**
- **Edge-optimized Endpoint** This actually uses the CloudFront Edge locations and offers reduced latency for requests from around the world.
- **Regional Endpoint** Reduced latency for requests that originate in the same region. Can also configure your own CDN and protect with WAF.
- **Private Endpoint** Securely expose your REST APIs only to other services within your VPC or connect via Direct Connect.

### Structure of REST API
- **Method Request** Similar to the commands that are available in HTTP
  - ANY
  - DELETE
  - GET
  - HEAD
  - OPTIONS
  - PATCH
  - POST
  - PUT
- **Integration Request** Map the request parameters of method request to the format required by the backend
  - HTTP
  - HTTP_PROXY
  - AWS (LAMBDA)
  - LAMBDA_PROXY
  - MOCK
- **Endpoint** the destination of the request
  - Lambda function,
  - HTTP Endpoint
  - EC2 instance
  - Other AWS service
- **Integration Response** Response from the endpoint
  - CONVERT
  - PASSTHROUGH
- **Method Response** Map the status codes, headers and payload received from the backend into format for the client (frontend)
  - HTTP STATUS CODES
  - RESPONSE BODIES


### API Gateway Integrations
- **Lambda Function**
  - **Lambda Proxy integration** - Passing the request as-is to Lambda  
  - **Lambda Custom integration** - Enables you to customize the request
- **HTTP endpoint**
  - **HTTP Proxy integration**
  - **HTTP Custom integration**
- **AWS Service** ONLY NON-PROXY TYPE FOR AWS SERVICES! 

### API GW Optimization
**Caching:**
- You can add caching to API calls by provisioning an AWS API GW cache and specifying its size in gigabytes
- Caching allows you to cache the endpoint's response
- Caching can reduce the number of calls to the backend and improve the latency of requests to the API
  
**Throttling:**
- API GW sets a limit on a steady-state rate and a burst of requests submissions against all APIs in your account
- Limits:
  - By default; steady-state request rate is limited to 10.000 requests per second
  - The maximum concurrent requests is 5000 requests across all API's within an AWS account
  - If you go over over these limits, you will receive a *429 Too Many Requests* error response.

### Usage Plans & API Keys
You can create different usage plans (basic and premium users) and define different throttling rates. 
  
- A throttling limit sets the target point at which request throttling should start. This can be set at the API or API method level.
- A quota limit sets the target maximum number of requests with a given API key that can be submitted within a specified time interval. You can configure individual API methods to require API key authorization based on usage plan configuration.
- Throttling and quota limits apply to requests for individual API keys that are aggregated across all API stages within a usage plan.
  
**API Keys**  
These can be used to grant a user access to your API. API GW can generate API Keys for you, or you can import them from a CSV file (external source).  
You can use API Keys together with Lambda authorizers, IAM roles and AWS Cognito.
  
You can also configure a per-method throttling limit.



