# EC2

## EC2 Lifecycle
- Stopped
  - EBS backed instances only
  - no charge
  - EBS volumes remain attached (charged)
  - RAM data is lost
  - instance is migrated to different host
  - Private IP addresses are retained, public IP address is released
- Hibernating EC2 instances
  - Applies to on-demand or reserved Linux instances
  - Contents of RAM saved to EBS volume
  - Must be enabled for hibernation when launched (+ specific prerequisites)
  - After starting: EBS is returned to previous state, RAM and processes are reloaded and instance ID is retained
- Reboot
  - Equivalent to an OS reboot
  - DNS name and IP addresses are retained
  - No effect on billing (it doesn't count as fully stopped)
- Retiring EC2 instances
  - May be done by AWS if AWS detects an irreparable failure of the hardware hosts
  - When an instance reaches its scheduled retirement, it is stopped or terminated by AWS
- Terminated
  - completely remove the instance
  - all data is lost (cannot recover instance)
  - by default; EBS volumes are deleted
- Recovering EC2 instances
  - If an instance has an underlying hardware/platform issue
  - Recovered instance is identical to the original instance

## AWS Nitro System
Nitro is the underlying platform (hardware) for the next generation of EC2 instances.   
It supports many virtualized and bare metal instance types. Bare Metal means excluding the hypervisor layer, which costs some resources.  
  
Nitro breaks the functions of the underlying infrastructure layer into specialised hardware with a Nitro Hypervisor:
- Nitro cards for VPC
- Nitro cards for EBS
- Nitro cards for Instance Storage
- Nitro cards controller
- Nitro security chip
- Nitro Hypervisor
- Nitro Enclaves
  
Nitro improves security, performance and innovation: 
- The performance for virtualized instances is close to bare metal. 
- Elastic Network Adapter and Elastic Fabric Adapter are Nitro based
- More bare metal instance types are supported
- Higher network performance (i.e. 100 Gbps)
- High Performance Computing (HPC) optimizations
- Dense storage instances (i.e. 60 TB)
  
**AWS Nitro Enclaves**  
- Isolated compute environments
- Runs on isolated and hardened virtual machines
- No persistent storage, interactive access or external networking
- cryptographic attestation to ensure only authorized code is running (very safe)
- Integrates with AWS KMS
- Protect and secure and process highly sensitive data:
  - Personally identifiable information (PII)
  - Healthcare data
  - Financial data
  - Intellectual Property data

## Bastion Host
 - `ssh -A` Enable forwarding of the authentication agent connection.
 - `ssh -i` identity file
 - `ssh-agent bash` start ssh agent and add path to ENV
 - `ssh-add <full-path-to-key>` add .pem file to active agent. ADD ABSOLUTE PATH! RELATIVE DOESN'T WORK!!

Bastion Host is an instance in your public subnet that you use to connect to your instances in a private subnet (forwarding your connection). You can also use the Bastion Host as a NAT instance (allow outbound, but block incoming internet traffic) for the private instances.

### Sources
- https://digitalcloud.training/ssh-into-ec2-in-private-subnet/
- https://www.ssh.com/academy/ssh/command
- https://unix.stackexchange.com/questions/48863/ssh-add-complains-could-not-open-a-connection-to-your-authentication-agent

### Result
![SA-1 EC2 Bastion Host](../../00_includes/SA-01/SA-01_EC2_BastionHost.png)
