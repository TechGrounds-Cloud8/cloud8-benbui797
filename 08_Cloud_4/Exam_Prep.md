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
- **Transit gateway:** A transit hub that can be used to interconnect multiple VPCs and on-premises networks, and as a VPN endpoint for the Amazon side of the Site-to-Site VPN connection. This is like a cloud router.
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

## Migration Services
- **AWS Snowball** Easily migrate terabytes of data to the cloud without limits in storage capacity or compute power. It is a physical device. 50/80TB. Snowball Edge 100TB. "Petabyte Scale".
- **AWS Snowcone** Similar to Snowball, but with 8TB of storage space.
- **AWS Snowmobile** Similar to Snowball, but an actual shipping container with 100PB (petabyte) storage space. Or you can move entire data centers. "Exabyte Scale".
- **AWS SMS (Server Migration Service)** Migrate servers and virtual machines to AWS EC2.
- **AWS DMS (Database Migration Service)** Migrate Databases to AWS. Can also be used to migrate from EC2 instance to RDS for example.
- **AWS AMS (Application Migration Service)** Migrate applications to AWS.
- **AWS DataSync** Simplify and accelerate secure data migrations, on-premises to cloud, vice-versa or AWS service to AWS service. Can be used with S3 and EFS.

## Machine Learning Services
- **AWS Rekognition** Image and video analysis
- **AWS Transcribe** Speech to text
- **AWS Translate** Translation AI
- **AWS SageMaker** Tool to train and deploy ML models
- **AWS Comprehend** NLP service, extract information from unstructured data.
- **AWS Lex** AI for Chatbots
- **AWS Polly** Text to Speech AI

## Additional Services
- **AWS Workspaces** Managed Desktop-as-a-service (DaaS) solution. Provide remote desktops for your employees.
- **AWS AppStream 2.0** Instead of streaming a desktop, stream a specific application.
- **AWS Worklink** Secure, one-click access to your internet websites using mobile phone browsers, without the requirement for a VPN or App.
- **AWS WorkDocs** AWS equivalent of Google Docs.
- **AWS IoT Core** Connect IoT devices to AWS Cloud. It's a managed service.
- **AWS Device Farm** Test your mobile or webapps by getting access to thousands of different mobile phones, desktops browers and tablets. Developers can easily test their applications across different platforms (automated). You can also get remote access and manually test things.


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
- **Amazon QuickSight** Amazon QuickSight is a fast, cloud-powered business intelligence service that makes it easy to deliver insights to everyone in your organization.
- **AWS Global Accelerator** Routes traffic to application endpoints through the AWS Global Network. It does not cache data (vs CloudFront)
- **AWS Cognito** Amazon Cognito lets you add user sign-up, sign-in, and access control to your web and mobile apps quickly and easily. Amazon Cognito scales to millions of users and supports sign-in with social identity providers, such as Apple, Facebook, Google, and Amazon, and enterprise identity providers via SAML 2.0 and OpenID Connect.  
- **AWS Directory Services** Integrate or manage MicroSoft Active Directory with AWS Cloud. AD Connector can be used as a SSO (single sign on). There is also Simple AD, powered by Samba 4 that is compatible with MS AD, but offers less features.
- **AWS STS** AWS STS is an AWS service that allows you to request temporary security credentials for your AWS resources, for IAM authenticated users and users that are authenticated in AWS such as federated users via OpenID or SAML2.0. It works similar to Access Keys, except their lifespan is much shorter (15 minutes to 36 hours typically).

# Synonyms and other terms
- **Elasticity** ability to scale up AND also down based on demand!
- **Horizontal Scaling** ability to add more instances/resources to share the workload; adding another harddrive
- **Vertical Scaling** increasing the capacity of a resource; installing a larger harddrive or faster CPU
- **High-Availability / Durability / Resilience** Spread out over multiple AZ's to increase reliability
- **Fault Tolerance** ability for your application to keep working even when a server has an error (for example, having multiple servers)
- **Provisioned** to provide (someone) with what is needed for a task or activity
- **Agility**  In a cloud computing environment, new IT resources are only a click away, which means that you reduce the time to make those resources available to your developers from weeks to just minutes. This results in a dramatic increase in agility for the organization, since the cost and time it takes to *experiment and develop* is significantly lower.
- **S3 access time synonyms** Rarely = Glacier, Infrequent = S3 IA, Non-often = ????? (there are 100+ synonyms, good luck!)

## To-Do

