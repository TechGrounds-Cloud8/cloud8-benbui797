- Healthchecks (ELB, ASG, R53, check configuration options and manual pages)
- https://aws.amazon.com/blogs/storage/turbocharge-amazon-s3-with-amazon-elasticache-for-redis/
- EBS Block Device Mapping??
- https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html
- EBS HDD use cases


## Backup / Disaster Recovery Strategies
- **Backup & Restore** A simple and low cost DR approach. This backups your data and applications from anywhere to the AWS cloud for use during recovery from a disaster. EC2 instances are only used as needed for testing, most of the data will be stored on S3 (Infrequent-Access).
- **Pilot Light** Analogy from gas heating, there is a small flame always on that can quickly ignite the entire furnace to heat up a house. In this DR approach, you replicate part of your IT infrastructure on a limited set of core AWS services so that the cloud can take seamlessly take over in the event of a disaster. A part of the infrastructure is always running simultaneously syncing mutable data (as databases or documents). In the case of a disaster, you can provision a full-scale production environment around the critical core.
- **Warm Standby** Warm Standby is used to describe a DR scenario where a scaled-down version of a fully functional environment is always running in the cloud. It extends the Pilot Light elements and preperation with not just the core, but all services. Recovery time is even smaller, because they are always on. It's important to identify your business-critical systems.
- **Multi-Site** A Multi-Site solution runs on AWS as well as your existing on-premises infrastructure in an *active-active* configuration. The data replication method that you employ will be determined by the recovery point that you choose (either RTO or RPO).