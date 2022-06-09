# Exam Prep

## AWS Site-to-Site VPN
By default, instances in your VPC can't communicate with your own (remote) network. You can enable this by creating a VPN.  
  
The following are the key concepts for Site-to-Site VPN:
- **VPN connection:** A secure connection between your on-premises equipment and your VPCs.
- **VPN tunnel:** An encrypted link where data can pass from the customer network to or from AWS. Each VPN connection includes two VPN tunnels which you can simultaneously use for high availability.
- **Customer gateway:** An AWS resource which provides information to AWS about your customer gateway device.
- **Customer gateway device:** A physical device or software application on your side of the Site-to-Site VPN connection.
- **Target gateway:** A generic term for the VPN endpoint on the Amazon side of the Site-to-Site VPN connection.
- **Virtual private gateway:** A virtual private gateway is the VPN endpoint on the Amazon side of your Site-to-Site VPN connection that can be attached to a single VPC.
- **Transit gateway:** A transit hub that can be used to interconnect multiple VPCs and on-premises networks, and as a VPN endpoint for the Amazon side of the Site-to-Site VPN connection.
- **AWS VPN CloudHub:** If you have multiple AWS Site-to-Site VPN connections, you can provide secure communication between sites using the AWS VPN CloudHub. This enables your remote sites to communicate with each other, and not just with the VPC.

## CodeCommit / CodeDeploy / CodePipeline  
- **CodeCommit** AWS version of GitHub (fully managed version control system)
- **CodeDeploy** Tool to automate deploy updates to applications
- **CodePipeline** Tool to help automatically deploy updates to applications (CI/CD)
  
## Security Hub
- Provides a comprehensive view of security alerts and security posture across AWS accounts.
- Aggregates, organizes and prioritizes security alerts, or findings from multiple AWS services.
- Continously monitors your environment using automated security checks.
- Configure security standards to validate against
  
**AWS Security Bulletins** News and notifications about  security & privacy events (such as a DDOS attack)
  
**AWS Trust & Safety Team**
Support team for: Spam, Port Scanning, DDOS, Intrustion attempts or hosting of objectionable or copyrighted content. Or distributing malware. abuse@amazonaws.com  
  
## Macie / Detective / GuardDuty / Inspector
- **AWS Macie** Machine Learning/AI that analyses your S3 for sensitive data (personal information, credit card numbers etc)
- **AWS Detective** Analyze, investigate and identify the root cause of potentional security issues or suspicious activities.
- **GuardDuty** Intelligent treath detection service. It can detect account compromise, instance compromise, and malicious activity
- **AWS Inspector** Amazon Inspector is a vulnerability management service that continuously scans your AWS workloads for vulnerabilities. Amazon Inspector automatically discovers and scans Amazon EC2 instances and container images residing in Amazon Elastic Container Registry (Amazon ECR) for software vulnerabilities and unintended network exposure.

## AWS Batch
Useful for when you need to run a large, resource intensive workload. You can upload your code, make a job definition and AWS will take care of the rest (it is a managed service).
  
## System Manager
Manages many AWS resources including EC2, S3 and RDS.
You can create documents (rules) and pass them to various components that will then perform some task.
Components are:
- **Automation** (i.e. make a snapshot of an RDS instance)
- **Run Command** (i.e. check EC2 instance for missing updates)
- **Inventory** (all kinds of data about the services, such as OS, installed applications, server roles)
- **Patch Manager** (deploy OS and software patches automatically across large groups of EC2 or on-premise instances)
- **Session Manager** (Secure remote management of your instances at scale without logging into your server (no SSH or PowerShell, so you don't need to open those ports))
- **Parameter Store** (provides secure, hierarchical storage for configuration data management and secrets management)

## AWS Storage Gateway
AWS Storage Gateway is a set of hybrid cloud storage services that provide on-premises access to virtually unlimited cloud storage. The data is encrypted in transit and can move via the internet of AWS Direct Connect.  
  
- **File Gateway** represents files as objects in S3 using NFS or SMB protocols
- **Volume Gateway** represents your applications block-storage volumes (EBS) using the iSCSI protocol. It can be used to make snapshots of on-premise volumes and store a backup in the cloud.
- **Tape Gateway** Tape Gateway presents an iSCSI-based virtual tape library (VTL) of virtual tape drives and a virtual media changer to your on-premises backup application. It is compatible with most leading backup applications, so you can continue using your tape-based backup workflows. 

## Databases
- **AWS Redshift** Data Warehouse
- **AWS EMR** Big Data Analytics based on Hadoop or Spark.
- **AWS Athena** Athena enables querying a Data Lake (S3) using SQL queries. Stores information and schema's about the databases & tables in AWS Glue.
- **AWS Glue** Metadata Catalog that you can use with Athena, S3 and Apache (Hive). It's a fully managed ETL service.
- **AWS ElastiCache** In-memory storage for ultra low latency (think of this as virtual RAM)
- **AWS Kinesis** Data Streams: For streaming data. Data Analytics: Provides real-time SQL processing before storing it. Data Firehose: Loads data straight into destinations.
- **AWS Data Pipeline** processes and moves data between different AWS resources.
- **AWS Quicksight** BI service. Enables you to create dashboards.
- **AWS Neptune** Fully managed Graph database.
- **AWS QLDB** Quantum Ledger Database aka AWS equavalent to blockchain. (immutable ledger db, cryptographically verifiable)
- **AWS Managed Blockchain** Fully Managed Service for joining public and private networks using Hyperledger Fabric and Ethereum.

## Cost Management / Budgets 

## Dedicated Host vs Dedicated Instances (LICENSE)
Physically seperated instance/server. You can use your own software licenses on Dedicated Hosts.  
**Dedicated Hosts = BYOL (BRING YOUR OWN LICENSE)**  
  
# Key terminology
- **Data Stream** Constant stream of information (stock prices, IoT data, geospatial data (uber), game data (statistics and results))
- **AWS Artifact** Library with AWS Compliance and Security documents.
- **Amazon Connect** Contact center for support etc.
- **AWS OpsWorks** AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet. Chef and Puppet are automation platforms that allow you to use code to automate the configurations of your servers. 
- **AWS Cloud Directory** directory-based storage. An object in a directory is intended to capture metadata (or attributes) about a physical or logical entity usually for the purpose of information discovery and enforcing policies. For example users, devices, applications, AWS accounts, EC2 instances and Amazon S3 buckets can all be represented as different types of objects in a directory.
- **AWS Managed Services (AMS)** helps you adopt AWS at scale and operate more efficiently and securely. Basically it is a (paid) helpdesk for operations. It can comply with ITIL and work with ITSM tools.
- **ITIL** Information Technology Infrastructure Library, the popular IT service management framework used by Enterprises. 
- **ITSM** Information Technology Service Management, 
- **AWS Health Dashboard** Here you can see information/news about Health issues that might impact your resources. Service Health, you can check if a service is online or not.
- **AWS Snowball** Easily migrate terabytes of data to the cloud without limits in storage capacity or compute power. It is a physical device.
- **AWS Snowcone** Similar to Snowball, but with 8TB of storage space.
- **AWS Snowmobile** Similar to Snowball, but an actual shipping container with 100PB (petabyte) storage space. Or you can move entire data centers.
- **Amazon QuickSight** Amazon QuickSight is a fast, cloud-powered business intelligence service that makes it easy to deliver insights to everyone in your organization.
- **AWS Global Accelerator** Routes traffic to application endpoints through the AWS Global Network. It does not cache data (vs CloudFront)
- **AWS Cognito** https://aws.amazon.com/cognito/?nc2=type_a


## To-Do

- ITSM tools / ITIL processes??? https://aws.amazon.com/managed-services/

- KSM vs CloudHSM

- https://aws.amazon.com/rekognition/image-features/

