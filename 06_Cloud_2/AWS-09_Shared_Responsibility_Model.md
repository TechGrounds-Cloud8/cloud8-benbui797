# AWS-09 Shared Responsibility Model
The Shared Responsibility Model describes who is responsible for what part of the cloud. As a general rule, the cloud provider is responsible for all the physical maintenance and security. The client/user is responsible for the configuration and proper usage (so setting up the firewall correctly, granting the right permissions and encrypting the right data).  
  
The model can differ for different services (IaaS, PaaS and SaaS). EC2 is an example of IaaS (Infrastructure as a service).  
  
IT Controls are another department which are shared between AWS and a client. By making use of the cloud service, part of these controls can be transferred to AWS, but the client remains responsible for another portion.  
  
**Inherited Controls** – Controls which a customer fully inherits from AWS.  
- Physical and Environmental controls
  
**Shared Controls** – Controls which apply to both the infrastructure layer and customer layers, but in completely separate contexts or perspectives. In a shared control, AWS provides the requirements for the infrastructure and the customer must provide their own control implementation within their use of AWS services. Examples include:  
  
- Patch Management – AWS is responsible for patching and fixing flaws within the infrastructure, but customers are responsible for patching their guest OS and applications.
- Configuration Management – AWS maintains the configuration of its infrastructure devices, but a customer is responsible for configuring their own guest operating systems, databases, and applications.
- Awareness & Training - AWS trains AWS employees, but a customer must train their own employees.
  
**Customer Specific** – Controls which are solely the responsibility of the customer based on the application they are deploying within AWS services. Examples include:  
  
- Service and Communications Protection or Zone Security which may require a customer to route or zone data within specific security environments.
  
![AWS-09 Shared Responsibility Model](../00_includes/CLOUD02/AWS-09_SRM1.jpg)
  
## Key terminology
- **IT controls** are procedures, policies and activities that are conducted to meet IT objectives, manage risks, comply with regulations and conform to standards.

## Exercise
### Sources
- Assessmentweek assignment
- https://aws.amazon.com/compliance/shared-responsibility-model/

### Overcome challenges
- N/A

### Results
- N/A
