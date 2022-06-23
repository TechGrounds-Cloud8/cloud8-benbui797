# Migration and Transfer
- **Hyper-V** MicroSoft Hyper-V is a type 1/bare-metal hypervisor 
- **VMware vSphere** is a virtualization platform and compromises a quite of virtualization products. ESXi hypervisor is approximating Hyper-V's capabilities. 
- **OVA** Open Virtualization Archive
  

## AWS Application Discovery Service
Collects data about servers in on-premises Data Centers.
- **VMware** Agentless discovery (OVA file in vCenter) - this collects all kinds of data; CPU, RAM, Disk I/O, Hostnames, Mac addresses, IP addresses, VM utilization, Disk Resource allocations
- **Hyper-V** Agent-based discovery (Windows/Linux) - collects all kinds of data and forwards it to App Discovery Service: Static Config data, Time-series perf data, Network I/O, Running Processes
  
Data allocated by ADS can be stored in S3 and queried with Athena/QuickSight.

- **Discovery Connector** Supported Servers: VMWare | Deployment: per vCenter | Collected Data: Static Config data, VM Utilization metrics | Supported OS: Any OS running in VMware vCenter (v5.5, v6, v6.5)
- **Discovery Agent** Supported Servers: VMware, Physical | Deployment: per Server | Collected Data: Static Config data, Time Series Performance Info (export), Network inbound/outbound (export), Running processes (export) | Supported OS: Amazon Linux, Ubuntu, RHEL, CentOS, SUSE, Windows Server
  
Discovery Connector is installed as a VM in your VMware vCenter and collects metadata that is send to the Discovery Service via SSL. It pings Application Discovery Service at 60 minute intervals for configuration information.
  
Hyper-V is considered physical, so you MUST use the agent (it needs to be installed) to collect the data. It is AWS software that you install on on-premises servers and VMs. It requires Root access. It will ping the Application Discovery Service at 15 minute intervals for configuration information.  

## AWS Data Migration Service
Helps migrate databases to AWS Databases. It can support migrations from on-premises to the cloud, but also EC2/RDS to another service migration.  
  
**Homogeneous Database Migrations**  
In Homogeneous Database Migrations the source and target database engines are the same or are compatible (Oracle to RDS Oracle or MySQL to Aurora). Since the schema structure, data types and database code are compatible between the source and target databases, this migration is a one-step process. You create a migration task with connections to the source and target and click "start", AWS DMS does the rest.  
  
**Heterogeneous Database Migrations**  
In heterogeneous database migrations, the source and target databases engines are different—like in the case of Oracle to Amazon Aurora, Oracle to PostgreSQL. In this case, the schema structure, data types and database code of the source and target databases can be quite different and require a *schema and code transformation* before the data migration starts.  
  
To prepare the source for the migration, you can use the **Schema Conversion Tool (SCT)**. This converts the source schema and code to match that of the target database. 
  
**Other Use Cases:**  
- **Migration between different AWS databases** - You can use AWS DMS to easily transfer data from a database running on EC2 to Aurora and vice versa.
- **Development and Test** - You can easily migrate data in or out of the cloud and make data copies to perform tests on. You can avoid disruption of the production database and perform tests and other tasks on the test database.
- **Database Consolidation** - You can use AWS DMS to consolidate multiple source databases into a single target database. The sources can come from different locations (on-premises, EC2, RDS).
- **Continuous Data Replication** - AWS DMS can be used to perform continuous data replication. This is useful for: Disaster Recovery instance synchronization, Geopgraphic database distribution (multi-region) and Dev/Test environment synchronization. It works for both homo- and heterogeneous data replication and from one-to-many or many-to-one target/source replications.


## AWS Server Migration Service
Helps migrate servers to EC2 instances

## AWS DataSync
Helps migrate storage systems to S3 of EFS.

## AWS Migration Hub
Unified console for all of the above. You can also monitor the used AWS or partner tools.