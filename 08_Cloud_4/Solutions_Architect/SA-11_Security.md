# Security
## AWS Directory Services
Active Directory is a MicroSoft service for IAM management that is used a lot in on-premises situations. 

**AWS Managed MicroSoft AD**  
- Fully Managed implementation of MicroSoft Active Directory running on Windows Server
- Highly Available pair of Windows Server **Domain Controllers (DC's)** - managed service
- One or two-way trust relationships (so you connect your whole network incl corporate office and EC2 instances)
- You can connect Azure AD or Office365 using **ADSync and ADFS**: synchronizes users and federate identities with Azure/O365.
  
- Best choice if you have more than 5000 users and/or need a trust relationship set up
- Can perform schema extensions
- Can setup trust relationships with on-premises Active Directories:
  - On-premise users and groups can access resources in either domain using SSO
  - Requires a VPN or Direct Connect connection
- Can be used as a standalone AD in the AWS Cloud
  
**AD Connector**  
- Used when you have an *existing* AD environment in your on-premises environment.
- Self-managed Microsoft AD
- Connect the local AD via VPN or Direct Connect to the AD Connector in the cloud
- You can then sign into AWS applications with AD credentials. This is a federated sign-in to AWS by mapping the Active Directory Identities to IAM Roles.
  
- *redirects directory requests* to your on-premise Active Directory
- Best choice when you want to integrate an existing Active Directory with AWS Services
- AD Connector comes in two sizes:
  - Small - organisations up to 500 users
  - Large - organisations up to 5000 users
- Requires a VPN or Direct Connect connection
- Can join an EC2 instance into your AD
- Login to the AWS Management Console using your on-premise AD DCs for authentication
  
**Simple AD**
- Inexpensive Active Directory-compatible service with common directory features
- Standalone, fully managed directory on the AWS cloud
- Least expensive option
- Best choice for < 5000 users and don't need advanced AD features
- Features include:
  - Manage user accounts/groups
  - Apply group policies
  - Kerberos-based SSO
  - Supports joining Linux or Windows based EC2 instances

## AWS Cognito
**User Pools**
Cognito acts as an *Identity Broker* between the IdP and WAS.
  
A client/mobile signs up or in via a *Cognito User Pool*, this returns an Token (JWT - Java Web Token). The client/mobile can then use this token to authenticate itself to the AWS. It connects to API gateway which then calls an *Lambda authorizer*(this accepts and processes the JWT).
  
We can connect SAML OIDC (Open ID Connect) applications into our User Pool (Facebook, Google, Apple accounts etc)  
    
**Identity Pool**  
Identity Pool is used to obtain *temporary, limited-privilege* credentials for AWS services. It uses AWS STS to do that.  
- Identities can come from an Cognito User Pool (but not only)
- Can also be connected to SAML OIDC
- STS grants an IAM role (federated user) which then grants access to the AWS services. 
  
- **User Pools** - Authentication (identity verification) - allows users to sign in through the user pool or federate through third-party identity provider (IdP)
- **Identity Pool** - Authorization (access control) - You can use identity pools to create unique identities for your users and give them access to other AWS services.
  
https://aws.amazon.com/premiumsupport/knowledge-center/cognito-user-pools-identity-pools/
  
## Web Application Firewall
- **Web ACL** - Web Access Control list (ACL) to protect a set of AWS Resources
- **Rules** - Each rule contains a statement that defines the inspection criteria and an action to take if a web request meets the criteria
- **Rule Groups** - You can use rules individually or in reusable rule groups
- **IP Sets** - A collection of IP addresses and IP Address ranges that you want to use together in a rule statement
- **Regex pattern set** - A regex pattern set provides a collection of regular expressions that you want to use together in a rule statement
  
- **Rule Action** - tells WAF what to do with a web request when it *matches* the criteria defined in the rule:
  - **Count** - WAF counts the request but doesn't detemine whether to allow of block it. With this action, WAF continues processing the remaining rules in the Web ACL
  - **Allow** WAF allows the request to be forwarded to the AWS resource for processing and response
  - **Block** WAF blocks the request and the AWS resource responds with an HTTP 403 (Forbidden) status code
  
- **Match Statement** - compare the web request or it's origin against conditions that you provide:
  - *Geographic match* inspects the country of origin
  - *IP set match* inspects the request against a set of IP addresses and adress ranges
  - *Regex pattern set* compares regex patterns against specified request component
  - *Size contraint* checks size constraints against a specified request component
  - *SQLi attack* inspects for malicious code in specified request component
  - *String match* Compares a string to a specified request component
  - *XSS scripting attack* inspects for cross-site scripting attacks in a specified request component

## AWS Inspector
- Runs assessments that check for security exposures and vulnerabilities on EC2 instances (and containers)
- Can be configured to run on a schedule
- Agent must be installed on EC2 for host assessments
- Network assessments do not require an agent
  
**Network Assessments**  
- Assessments: Network configuration analysis to check for ports reachable from outside the VPC
- If the Inspector Agent is installed on your EC2, the assessment also finds processes reachable on port
- Price is based on the number of instance assessments
  
**Host Assessments**
- Assessments: 
  - Vulnerable Software (CVE - Common Vulnerabilities and Exposures)
  - Host hardening (CIS benchmarks)
  - Security best practises
- Requires an agent (auto-install with SSM Run Command)
- Price is based on the number of instance assessments
