# AWS-01 Global Infrastructure
In the cloud, everything from servers to networking is virtualized. As an AWS customer, you don’t have to worry about the underlying physical infrastructure. That being said, the physical location of an application in the cloud can be important.  
  
AWS has a global infrastructure made up of the following components:  
- Regions
- Availability Zones
- Edge Locations
  
As a customer, you have different amounts of control over where your stuff is located depending on the service you use.  
For example, IAM is a global service, so you get no control over where its information is stored. In contrast, you can select specific Availability Zones for RDS instances.  
  
## Key terminology
- **AWS Region**: An AWS Regions is a geographic area where multiple AZ's are located.
- **AWS AZ**: An AWS Availability Zone consists of one or more discrete data centers. 
- **AWS Local Zones**: AWS Local Zones place compute, storage, database, and other select AWS services closer to end-users.
- **High Availability**: Not being dependent on a single data center. This enables easy failovers, reduces latency and ensures there is always a data center available. 
- **AWS Cloudfront**: An AWS Service that stores your data in AWS partner's data centers around the world, reducing latency by routing traffic to the nearest Edge.
- **Edge Location**: A data center of an AWS Partner that is used for the AWS backbone network (and AWS Cloudfront).

## Exercise
### Sources
- https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- https://aws.amazon.com/cloudfront/features/?p=ugi&l=emea&whats-new-cloudfront.sort-by=item.additionalFields.postDateTime&whats-new-cloudfront.sort-order=desc
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html
- https://bytequest.net/choosing-aws-region/

### Overcome challenges
N/A

### Results
**What is a Region?**  
AWS has the concept of a Region, which is a physical location around the world where Data Centers are clustered. Each group of logical data centers is called and Availability Zone (AZ). Each AWS Region consists of multiple, isolated and physically seperate AZ's within a geopgrahic area. Other Cloud Providers often define a region by a single data center. Since AWS Regions are split into multiple AZ's, every AZ has it's own power, cooling and physical security. This ensures high availability.  
  
**What is an AWS Availability Zone?**  
An Availability Zone (AZ) is one or more discrete data centers with redundant power, networking, and connectivity in an AWS Region. AZs give customers the ability to operate production applications and databases that are more highly available, fault tolerant, and scalable than would be possible from a single data center. All AZs in an AWS Region are interconnected with high-bandwidth, low-latency networking, over fully redundant, dedicated metro fiber providing high-throughput, low-latency networking between AZs. All traffic between AZs is encrypted. The network performance is sufficient to accomplish synchronous replication between AZs. AZs make partitioning applications for high availability easy. If an application is partitioned across AZs, companies are better isolated and protected from issues such as power outages, lightning strikes, tornadoes, earthquakes, and more. AZs are physically separated by a meaningful distance, many kilometers, from any other AZ, although all are within 100 km (60 miles) of each other.
    
**What is an Edge Location?**  
Amazon CloudFront is a web service that speeds up distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you're serving with CloudFront, the request is routed to the edge location that provides the lowest latency (time delay), so that content is delivered with the best possible performance.
  
**Why would you choose one region over another? (e.g. eu-central-1 (Frankfurt) over us-west-2 (Oregon)).**  
If most of your clients are from a specific geographic location (say NL), it makes sense to choose the nearest region. This reduces latency for the clients. This is not the only factor to keep in mind though;
- Cost
- Performance
- Features
- Availability
  
**Cost**  
The cost for different AWS services can vary by region. If you require a specific service that is expansive, it may be optimal to choose a different region (if the cost is more important than the latency).  
  
**Performance**  
If your users are more widespread, you may pick a region that provides the lowest latency to the regions where your clients are. You can use [this website](https://www.cloudping.co/grid) to check the latency between regions.  
  
**Features**  
Not all features are available in all regions. You can [use this link](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) to check whether the required features are available.  
  
**Availability**  
AZ's enable to design apps with automatic failovers, so AZ's are key to availability and fault tolerance. Different regions have a different amount of AZ's available. Some regions have 2, whilst others have 3 or more. If an app requires high availability, it may be desirable to choose a region with 3 or more AZ's.


