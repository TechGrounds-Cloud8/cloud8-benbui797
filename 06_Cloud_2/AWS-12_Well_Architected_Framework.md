# AWS-12 Well Architected Framework
The AWS Well Architected Framework helps Cloud Architects build secure, high-performing, resilient and efficient infrastructure for different applications and workloads. It is build around six pillars:
- Cost Optimization
- Reliability
- Operational Excellence
- Performance Efficiency
- Security
- Sustainability

AWS has them in a different order, but this way, the donkey bridge is "CROPSS". If you have good crops, you have a good harvest =)  
  
The Well-Architected Framework consists of key concepts, design principles and architectural best practises. These have been categorised under the six pillars. By asking a few foundational questions, you can evaluate your new  and current architectures and designs and see how well they align with the best practises. Besides that, you can also receive feedback for making improvements.  
  
## Operational Excellence Pillar  
The operational excellence pillar focuses on running and monitoring systems, and continually improving processes and procedures. Key topics include automating changes, responding to events, and defining standards to manage daily operations.  
  
There are 5 design principles for Operational Excellence:
1. **Perform operations as code (IaC):** You can define and script your entire workload as code. This way you can script events (conditionals) and make your code respond to them automatically and consistenly. This also reduces the risk of human error.
2. **Make frequent, small, reversible changes:** Design your workloads in a way that allows for small, frequent changes and updates. If an update does not work, it should be easy to revert it (without affecting the customer).
3. **Refine operations procedures frequently:** Refine the procedures you follow to deploy architectures regularly. Plan in moments where you review if all operations are efficient and everyone in the team is familiar with them.
4. **Anticipate failure:** Perform “pre-mortem” exercises to identify potential sources of failure so that they can be removed or mitigated. Test your failure scenarios and validate your understanding of their impact. Test your response procedures to ensure they are effective and that teams are familiar with their execution. Set up regular game days to test workload and team responses to simulated events.
5. **Learn from all operational failures:** Drive improvement through lessons learned from all operational events and failures. Share what is learned across teams and through the entire organization.
    
## Security Pillar  
The security pillar focuses on protecting information and systems. Key topics include confidentiality and integrity of data, managing user permissions, and establishing controls to detect security events.  
  
There are 6 design principles for Security:  
1. **Implement a strong identity foundation:** Implement the principle of least privilege and enforce the appropriate authorization for every interaction with AWS resources. Centralize Identity Management and avoid long-term static credentials.
2. **Enable traceability:** Monitor, alert and audit actions and changes to your environment in real time. Integrate log and metric collection with systems to automatically investigate and take action.
3. **Apply security at all layers:** Apply a defense in depth approach with multiple security controls. Apply to all layers (for example, edge of network, VPC, load balancing, every instance and compute service, operating system, application, and code).
4. **Automate security best practices:** Automated software-based security mechanisms improve your ability to securely scale more rapidly and cost-effectively. Create secure architectures, including the implementation of controls that are defined and managed as code in version-controlled templates.
5. **Protect data in transit and at rest (stored):** Classify your data into sensitivity levels and use mechanisms, such as encryption, tokenization, and access control where appropriate.
6. **Keep people away from data:** Use mechanisms and tools to reduce or eliminate the need for direct access or manual processing of data. This reduces the risk of mishandling or modification and human error when handling sensitive data.
7. **Prepare for security events:** Prepare for an incident by having incident management and investigation policy and processes that align to your organizational requirements. Have an Incident Response Plan ready. Run incident response simulations and use tools with automation to increase your speed for detection, investigation, and recovery.

## Reliability Pillar  
The reliability pillar focuses on workloads performing their intended functions and how to recover quickly from failure to meet demands. Key topics include distributed system design, recovery planning, and adapting to changing requirements.  
  
There are 5 best practises for Reliability in the cloud:
1. **Automatically recover from failure:** By monitoring a workload for key performance indicators (KPIs), you can trigger automation when a threshold is breached. These KPIs should be a measure of business value, not of the technical aspects of the operation of the service. This allows for automatic notification and tracking of failures, and for automated recovery processes that work around or repair the failure. With more sophisticated automation, it’s possible to anticipate and remediate failures before they occur.
2. **Test recovery procedures:** Test how your workload fails so you can validate your recovery procedures. You can use automation to simulate different failures or recreate scenarios that led to failures before. This way you can find and fix weaknesses before a real scenario occurs.
3. **Scale horizontally to increase aggregate workload availability:** Replace one large resource with multiple small resources to reduce the impact of a single failure on the overall workload. Distribute requests across multiple, smaller resources to ensure that they don’t share a common point of failure.
4. **Stop guessing capacity:** Monitor demand and workload utilization, and automate the addition or removal of resources to maintain the optimal level to satisfy demand without over- or under-provisioning.
5. **Manage change in automation:** Changes to your infrastructure should be made using automation. The changes that need to be managed include changes to the automation, which then can be tracked and reviewed.
  
## Performance Efficiency Pillar
The performance efficiency pillar focuses on structured and streamlined allocation of IT and computing resources. Key topics include selecting resource types and sizes optimized for workload requirements, monitoring performance, and maintaining efficiency as business needs evolve.  
  
These are the design principles to maintain and achieve efficient workloads:  
1. **Democratize advanced technologies:** Make use of advanced (cloud) technology that makes the life of your IT team easier. For example; NoSQL databases, Media Transcoding and Machine Learning are complex tasks that require specialised expertise. In the cloud you can use these as a service and allow your team to focus on product development instead of resource provisioning and management.
2. **Go global in minutes:** Deploying your workload in multiple AWS Regions around the world allows you to provide lower latency and a better experience for your customers at minimal cost.
3. **Use serverless architectures:** Serverless architectures remove the need for you to run and maintain physical servers for traditional compute activities. For example, serverless storage services can act as static websites (removing the need for web servers) and event services can host code. This removes the operational burden of managing physical servers, and can lower transactional costs because managed services operate at cloud scale.
4. **Experiment more often:** With virtual and automatable resources, you can quickly carry out comparative testing using different types of instances, storage, or configurations.
5. **Consider mechanical sympathy:** Use the technology approach that aligns best with your goals. For example, consider data access patterns when you select database or storage approaches.
  
## Cost Optimization Pillar
The cost optimization pillar focuses on avoiding unnecessary costs. Key topics include understanding spending over time and controlling fund allocation, selecting resources of the right type and quantity, and scaling to meet business needs without overspending.  
  
For Cost Optimization, there are the following design principles:
1. **Implement cloud financial management:** To achieve financial success and accelerate business value realization in the cloud, you must invest in Cloud Financial Management. Your organization must dedicate the necessary time and resources for building capability in this new domain of technology and usage management. Similar to your Security or Operations capability, you need to build capability through knowledge building, programs, resources, and processes to help you become a cost efficient organization.
2. **Adopt a consumption model:** Pay only for the computing resources you consume, and increase or decrease usage depending on business requirements. For example, development and test environments are typically only used for eight hours a day during the work week. You can stop these resources when they’re not in use for a potential cost savings of 75% (40 hours versus 168 hours).
3. **Measure overall efficiency:** Measure the business output of the workload and the costs associated with delivery. Use this data to understand the gains you make from increasing output, increasing functionality, and reducing cost.
4. **Stop spending money on undifferentiated heavy lifting:** AWS does the heavy lifting of data center operations like racking, stacking, and powering servers. It also removes the operational burden of managing operating systems and applications with managed services. This allows you to focus on your customers and business projects rather than on IT infrastructure.
5. **Analyze and attribute expenditure:** The cloud makes it easier to identify and divide the cost and usage of workloads over the corresponding departments. This helps measure ROI and gives the workload owners an opportunity to optimize their resources and reduce costs.

## Sustainability Pillar
The sustainability pillar focuses on minimizing the environmental impacts of running cloud workloads. Key topics include a shared responsibility model for sustainability, understanding impact, and maximizing utilization to minimize required resources and reduce downstream impacts.
  
In my personal opinion, this pillar doesn't add anything new. It more or less a replication of the cost and performance efficiency pillars, but now the result is an environmental improvement instead of one for the costs or performance...
  
In order to maximize sustainability and minimize impact, you can follow these design principles:
1. **Understand your impact:** Measure the impact of your cloud workload and model the future impact of your workload. Include all sources of impact, including impacts resulting from customer use of your products, and impacts resulting from their eventual decommissioning and retirement. Compare the productive output with the total impact of your cloud workloads by reviewing the resources and emissions required per unit of work. Use this data to establish key performance indicators (KPIs), evaluate ways to improve productivity while reducing impact, and estimate the impact of proposed changes over time.
2. **Establish sustainability goals:** For each cloud workload, establish long-term sustainability goals such as reducing the compute and storage resources required per transaction. Model the return on investment of sustainability improvements for existing workloads, and give owners the resources they need to invest in sustainability goals. Plan for growth, and architect your workloads so that growth results in reduced impact intensity measured against an appropriate unit, such as per user or per transaction. Goals help you support the wider sustainability goals of your business or organization, identify regressions, and prioritize areas of potential improvement.
3. **Maximize utilization:** Right-size workloads and implement efficient design to ensure high utilization and maximize the energy efficiency of the underlying hardware. Two hosts running at 30% utilization are less efficient than one host running at 60% due to baseline power consumption per host. At the same time, eliminate or minimize idle resources, processing, and storage to reduce the total energy required to power your workload.
4. **Anticipate and adopt new, more efficient hardware and software offerings:** Support the upstream improvements your partners and suppliers make to help you reduce the impact of your cloud workloads. Continually monitor and evaluate new, more efficient hardware and software offerings. Design for flexibility to allow for the rapid adoption of new efficient technologies.
5. **Use managed services:** Sharing services across a broad customer base helps maximize resource utilization, which reduces the amount of infrastructure needed to support cloud workloads. For example, customers can share the impact of common data center components like power and networking by migrating workloads to the AWS Cloud and adopting managed services, such as AWS Fargate for serverless containers, where AWS operates at scale and is responsible for their efficient operation. Use managed services that can help minimize your impact, such as automatically moving infrequently accessed data to cold storage with Amazon S3 Lifecycle configurations or Amazon EC2 Auto Scaling to adjust capacity to meet demand.
6. **Reduce the downstream impact of your cloud workloads:** Reduce the amount of energy or resources required to use your services. Reduce or eliminate the need for customers to upgrade their devices to use your services. Test using device farms to understand expected impact and test with customers to understand the actual impact from using your services.
  
# Key terminology
- **Distributed System** Back in the day, a server that connected multiple clients to a printer was considered a distributed system. Nowadays it can be much more complex. Distributed System can cover: Distributed Realtime Sytems (Flight Control), Parallel Processing (in the cloud) and Distributed Database Systems (The database is split over multiple servers and/or physical locations)
- **Outcome vs Output** Outcome is a driver, behaviour, skill or capacity that produces a specific business result. Output is an tangible deliverable (an email, a storyboard)
- **Business Output** In economics, output is the total quantity of goods and services that an individual, company, industry, city, region or country, or even the whole world produces in a given period. 
- **Well-Architected Lenses** These lenses extend the framework for specific industry domains, such as gaming, streaming, data analytics, machine learning and more.
- **Well-Architected Tool** A tool that you can use to review the architecture against the best practises defined by the Well-Architected Framework. You can also apply custom Lenses.
  

## Exercise
### Sources
- https://aws.amazon.com/architecture/well-architected/
- https://www.confluent.io/learn/distributed-systems/
- https://www.riskology.co/pre-mortem-technique/
- https://marketbusinessnews.com/financial-glossary/output-definition-meaning/
- https://www.strategydriven.com/tag/business-output/

### Overcome challenges
- Learning about some business terms: Pre-Mortem Technique, Business Output
