# Databases

# RDS
RDS runs on EC2 instances, you specify the instance when you launch RDS. By selecting a more powerful instance, you can vertically scale your database.

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
  
Cluster Mode enabled: Multiple Shards!
Cluster Mode disabled: Single Shard!  

## DynamoDB

- You can configure Time To Live (TTL) - expiry date for an item in a table
- No extra cost and does not consume WCU/WCU
- Helps reduce storage and manage the table size over time


  

# Todo
- Check out how Transactional Logs work