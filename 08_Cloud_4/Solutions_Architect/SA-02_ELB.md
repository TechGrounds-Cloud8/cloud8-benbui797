# ELB

## Types
**ALB**  
- Can route requests based on the path in the url (layer 7) *www.example.com/pathexample*
- Host-based routing is also possible (based on the host field in HTTP header -> sends it to specified target group) *hostexample.example.com*
  
**NLB**  
- NLB nodes can have *elastic IPs* in each subnet
- The nodes in each subnet are the targets. These forward the requests to the instances in that subnet.
- Its layer 4 (IP protocol) so it can have a listener for different ports. (TCP / port 80 for HTTP routing - HTTP is layer 7, so that doesnt work!)
- Targets can be outside of VPC (on-premises)
- Targets can be EC2 instances or an IP Address

Cross-Zone load balancing is enabled for ALB by default. It helps evenly spread out the load between instances in different AZs. It is disabled for NLB's by default.

## Sessions
- **Session-State Data** Store data in another resource (DynamoDB, ElastiCache or sometimes S3). If an instance fails, the users authentication isn't lost and he doesn't need to re-authenticate.
- **Sticky Sessions** When a client connects, a cookie is generated and bounds the client to an instance for cookie lifetime. Data is stored locally, so if an instance fails, the data is lost. 
  
Both can be used together.  


# Todo
- Try to set up an NLB that is targetting 2 ALBs