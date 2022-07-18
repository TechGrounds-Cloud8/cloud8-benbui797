# Databases

# RDS
RDS runs on EC2 instances, you specify the instance when you launch RDS. By selecting a more powerful instance, you can vertically scale your database.  
  
RDS Multi-AZ deployment (one standby) == Synchronous replication (failover backup instance for disaster recovery)  
  
RDS Multi-AZ deployment (read-replica's) == Asynchronous replication 

RDS Single-AZ == No read replica's!!


## Backups & Maintenance
**Automated Backups**
- You can select a backup window (e.g. every hour or every day)
- A snapshot is taken which is stored for teh retention period (max 35 days)
- You can do a point-in-time recovery for any snapshot taken within the retention period.
  
**Manual Backups**
- Backs up the entire DB instance, not just the individual database
- For single-AZ DB instances, there is a suspension of I/O operations
- For Multi-AZ SQL server; I/O is briefly suspensed on primary db
- For Multi-AZ MariaDB, MySQL, Oracle and PostgreSQL the snapshot is taken from the standby
- Snapshots do not expire (no retention period)
  
**Maintenance Windows**
- OS and Database patching can require taking the database online
- These tasks take place during a maintenance window
- By default a weekly maintenance window is configured
- You can select your own maintenance window
  
## Security / Encryption
- **A READ REPLICA MUST HAVE THE SAME ENCRYPTION SETTING AS THE PRIMARY!**
- The same KMS key is used if both instances are in the same region
- If the read replica is in a different region, a different KMS key is used
- You can't restore an unencrypted backup or snapshot to an encrypted DB instance
  
**Create Encypted Copy of DB**  
- You can copy an unencrypted Snapshot and encrypt the snapshot copy.
- Then restore instance from the encypted snapshot
- You now have a new DB with the same data as before, but with encryption. The DB instance is completely new (so a new endpoint)

## Aurora
- https://digitalcloud.training/courses/aws-certified-solutions-architect-associate-hands-on-labs/sections/section-12-databases-and-analytics-2hr-15m/lessons/amazon-aurora-deployment-options-3/
  
Write all the deployment options

### Aurora Storage Engine
Aurora has its own storage system. Aurora Instances are all connected to a **Cluster volume**, which is seen as a single data volume, but consists of many parts. The storage that can automatically scale in size. It scales in 10 GB increments (logical blocks), also known as *Protection Group*. Within the protection groups, the data is replicated across 6 storage nodes and across 3 AZ's.  
Aurora Storage can scale up to 64TiB (and for some DB engines, 128TiB)

- https://aws.amazon.com/blogs/database/introducing-the-aurora-storage-engine/

## ElastiCache
- Fully managed implementations of *Redis* and *Memcached*
- its a key/value store
- in-memory database offering high performance and low-latency
- Can be put in front of databases such as RDS or DynamoDB
- ElastiCache nodes run on EC2 instances, so you must choose an instance type
  
**Memcached**
- Data is not persistent
- Used for *simple* data types
- Data is partitioned (each node is a partition of data)
- No encryption
- No high availability (no data replication)
- Can launch nodes in multiple AZ's, but there is no failover or replication
- Scaling: Up (node type - must create a new cluster manually); Out (add nodes)
- Multithreaded
- No backups and restoration possible (no snapshots)
  
**Redis (Cluster mode disabled)**  
- Data is persistent
- Used for *more complex* data types
- Data is not partitioned
- Can be encrypted
- High availability
- Auto-failover and read replica's (0-5 per shard)
- Scaling: Up (node type); Out (add replica)
- No Multithreading
- Automatic and manual snapshots
  
**Redis (Cluster mode enabled)**  
- Data is persistent
- Used for *more complex* data types
- Data is not partitioned
- Can be encrypted
- High availability
- Auto-failover and read replica's (0-5 per shard)
- Scaling: Up (node type); Out (add shard)
  - Online resharding to add or remove shards; vertical scaling to change node type
  - Offline resharding to add or remove shards, change node type or upgrade engine (more flexible than online)
- No Multithreading
- Automatic and manual snapshots
  
A **Shard** in Redis mode consists of a primary plus zero to five replica's. A shard can cover multiple AZs (across multiple AZ's).  
  
Sharding means adding more partitions (so storing some keys/hashes on one shard and other keys on another), this improves performance. It spreads out the data over multiple shards.
  
Cluster Mode enabled: Multiple Shards!
Cluster Mode disabled: Single Shard!  
  
## AWS RedShift
- Fast, fully managed Data Warehouse
- Analyse data using SQL or Business Intelligence Tools
- RedShift is a SQL based data warehouse used for analytics applications
- RedShift is used for OLAP (Online Analytics Processing)
- RedShift uses EC2 instances, so you must choose an instance type
- RedShift always keeps 3 copies of your data
- RedShift provides continuous/incremental backups
- RedShift Data Sources:
  - EC2
  - AWS Glue
  - AWS Data Pipeline
  - AWS S3
  - AWS EMR
  - AWS DynamoDB
  - AWS RDS
  - On-Premises Server

- **RedShift Spectrum** can run SQL queries on data directly in S3 (Athena can too, but with RedShift you have control over the resources (Instances), which can allow for more consistent performance)
  
Use Cases:
- Perform complex queries on huge collections of structured and semi-structured data and get fast performance
- Frequently accessed data that needs a consistent highly structured format
- Use *Spectrum* for direct access of S3 Objects in a data lake
- Managed data warehouse solution with:
  - Automated provisioning, configuration and patching
  - Data durability with continuous backup to S3
  - Scales with simple API calls
  - Exabyte scale query capability

## Amazon OpenSearch Service
**Summary:**
- Distributed search and analytics suite
- Based on the popular open source Elasticsearch
- Supports queries using SQL syntax
- Integrates with open-source tools
- Scale by adding or removing instances
- Availability in up to three AZ's
- Backup using snapshots
- Encryption at rest & in transit
  
**Deployment:**
- Clusters are created (through console, API or CLI)
- Clusters are also known as OpenSearch Service domains
- You specify the number of instances and instance types
- Storage options include UltraWarm (S3 + sophisticated caching) or Cold storage (S3). standard is called "Hot" and uses Instance Stores (EBS)
  
**Ingesting Data into OpenSearch Service domain:**
- AWS Kinesis Data Firehose
- Logstash
- Elasticsearch / OpenSearch API
  
Then attach a Kibana Dashboard to search, visualize and analyze data.

**Limitations:**  
- You can launch a cluster in an VPC, but you can not use IP-based access policies
- VPN or Proxy required to connect from the internet (public domains are directly accessable)
- You can't switch from VPC to a public endpoint. The reverse is also true
- You can't launch your domain within a VPC that uses dedicated tenancy.
- After you place a domain within a VPC, you can't move it to a different VPC, but you can change the subnets and security group settings.
  
**The ELK Stack**
- ELK = Elasticsearch, Logstash and Kibana
- Popular combination of projects
- Aggregate logs from systems and applications, analyze these logs and create visualizations
- Use cases:
  - Visualizing application and infrastructure monitoring data
  - Troubleshooting
  - Security Analytics

## AWS Athena / AWS Glue
- Athena optimisation: https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/

# OLTP vs OLAP
OLTP: RDS / Aurora  
OLAP: RedShift  

# Todo
- Check out how Transactional Logs work
- Check out the Hands-On Lessons
- Check out Exam Cram

