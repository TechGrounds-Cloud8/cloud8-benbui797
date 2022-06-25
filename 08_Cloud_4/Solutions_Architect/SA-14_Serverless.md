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
- SQS, Kinesis Data Streams, DynamoDB Streams
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
| Service | What It Does | Example Use Cases |
________________________________________________
| Simple Queue Service | Messaging queue; store and forward patterns | Building distributed / decoupled apps |

- https://digitalcloud.training/courses/aws-certified-solutions-architect-associate-hands-on-labs/sections/section-11-serverless-applications-1hr-30m/lessons/application-integration-services-overview-2/

## SQS
