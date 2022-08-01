# AWS-13-3 Route53
Route53 is a Domain Name System (DNS) web service. It enables developers to connect internet users to WebApps by translating names to IP addresses. It works with both IPv4 and IPv6.  
It can be used to route user requests to infrastructure running in AWS (EC2, ELB, S3 etc), but also infrastructure outside of AWS.  
  
**Domain Registration**  
One of the core functions of Route53 is the ability to register domain names (www.example.com or www.example.lol or anything else that is available). After you have registered a domain, Route53 automatically creates a public Hosted Zone.
  
**Hosted Zone**  
A Hosted Zone contains information about how you want to route internet traffic for a specific domain and its subdomains. One of the things you add here is which IP address should correspond to which DNS name. 
You either get a Hosted Zone once you register a domain with Route53, or you start by creating one when you transfer an existing domain registration to Route53.  
  
It is also possible to create a private Hosted Zone. Using that, you can route traffic within an AWS VPC. Essentially, you can now connect to your AWS Resources via a name defined in the Hosted Zone instead of their IP addresses.  

**Health Checks**  
Route53 can be used to perform health checks on your resources and additionally can be linked to a CloudWatch alarm and SNS.  
You can define what protocols should be used for a health check (*http, https or tcp*), how often the check should be done (*request interval*) and how many times a request should fail before a resource is considered unhealthy (*failure treshhold*).  
If you run multiple resources with the same function (i.e. web servers), you can configure a *DNS Failover* which means, if Route53 notices a unhealthy resource, it'll route traffic away from it.  

**Traffic Flow**  
Traffic flow are the collection of a number of options that control how traffic gets routed via Route53. One of the main elements are Traffic Policies.  
You can have multiple options for routing policies such as: 
- Simple routing policy – Use for a single resource that performs a given function for your domain, for example, a web server that serves content for the example.com website.
- Failover routing policy – Use when you want to configure active-passive failover.
- Geolocation routing policy – Use when you want to route traffic based on the location of your users.
- Geoproximity routing policy – Use when you want to route traffic based on the location of your resources and, optionally, shift traffic from resources in one location to resources in another.
- Latency routing policy – Use when you have resources in multiple AWS Regions and you want to route traffic to the region that provides the best latency.
- IP-based routing policy – Use when you want to route traffic based on the location of your users, and have the IP addresses that the traffic originates from.
- Multivalue answer routing policy – Use when you want Route 53 to respond to DNS queries with up to eight healthy records selected at random.
- Weighted routing policy – Use to route traffic to multiple resources in proportions that you specify.
  
**CNAME vs Alias Records**  
*CNAME*  
- CNAME can point any DNS query to any other DNS record (even non Route53). Never to an IP address. 
- AWS charges you for CNAME queries
- A CNAME record can't be at the top node of a DNS namespace (zone apex)
  
*Alias Record*  
- An Alias Record can only point to a CloudFront distribution, Elastic Beanstalk, ELB, S3 bucket (static website) or to another record in the same hosted zone that the alias record is in.
- You do not get charged for alias queries to AWS Resources.
- You can create an Alias Record at the zone apex (but you cannot route to a CNAME at the zone apex).



## Key terminology
- **Domain Name System (DNS)** This is the protocol that translates named adresses (for humans) to IP addresses (for computers). 

## Exercise
### Sources
- https://aws.amazon.com/route53/
- https://aws.amazon.com/route53/what-is-dns/
- https://ns1.com/resources/cname

### Overcome challenges
- I knew what DNS was and it's usecase, but I went much deeper on the subject for this assignment. Now I also learned about the inner workings, that it consists of multiple layers and how the traffic is actually routed.

### Results
-N/A
