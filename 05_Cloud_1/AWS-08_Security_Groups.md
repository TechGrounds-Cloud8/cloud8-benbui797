# AWS-08 Security Groups
A security group acts as a virtual statefull firewall for EC2 instances. It controls incoming (inbound rules) and outgoing (outbound rules) traffic to and from the instance.  
    
Security Groups do not run on the OS, but in the VPC. That means you can add one or more (up to 5) security groups to an instance. Multiple instances can share the same security group(s). 
  
I think of security group as firewall blueprints. They only have allow rules. You need to explicitly allow traffic, otherwise it's implicitly denied. If you change the configuration for a SG, it is automatically applied to all instances associated with the group.

Security is a shared responsibility. Amazon provides security groups, but it's up to the client to configure them correctly. If they do not meet all demands, you can run an additional firewall on the instances.
  
A network access control list (NACL) is an additional way to control traffic in and out of one or more subnets. Unlike AWS Security Groups, NACLs are stateless, so both inbound and outbound rules will get evaluated. Every rule gets a number assigned to them (this determines the order of evaluation). Network ACLs can be set up as an optional, additional layer of security to your VPC. By default, they allow all in- and outgoing traffic.  
  
NACL are useful to create an additional layer of protection for, for example, a database server that is connected on a specific subnet. 


## Key terminology
- **SG** Security Group
- **NACL** Network Access Control List
- **VPC** refers to Virtual private Cloud, which can be visualized as a container that stores subnets. Subnets can be considered as a container, which helps store data. 
- **inbound rules** aka the source. These rules talk about the source from where the request or traffic is coming from, and about the destination port/ the port through which the response is sent.
- **outbound rules** aka the destination. These rules talk about where the response should be sent and about the destination port. 
- **Default NACL** by default, the NACL allows all in- and outgoing traffic
- **Custom NACL** by default, a custom NACL denies all in- and outgoing traffic. You have to specify the allow rules once you have created/assigned a custom NACL.
- **numbering NACL rules** it's best practise to increment the rules in steps of 10 or 100. This way, you can insert new rules later on.
  

## Exercise
### Sources
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html
- https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html?ref=wellarchitected
- https://www.checkpoint.com/cyber-hub/cloud-security/what-is-aws-security-groups/
- https://www.knowledgehut.com/tutorials/aws/aws-nacl
- https://www.knowledgehut.com/tutorials/aws/nacl-vs-security-groups

### Overcome challenges
- I misunderstood the EC2 assignment and had already read about SG's (and created a custom one). However, now I did a little deep-dive and learned more about their practical use, plus their relation with and to NACL's.

### Results
N/A
