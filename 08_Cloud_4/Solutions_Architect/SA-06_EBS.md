# EBS

## EBS Multi-Attach
- Must be within a single AZ
- Only available for Nito system-based EC2 instances
- Must be a Provisioned IOPS SSD volume
- Max. 16 instances can be attached to a single volume

## EBS SSD Volumes
Provisioned IOPS are the fastest volume types and always run on SSD.  

https://aws.amazon.com/ebs/provisioned-iops/
 ## EBS HDD Volumes
 **You cannot have HDD Volumes as your boot volume!!**
   
- Throughput Optimized HDD - Big Data, Data warehouses and log processing
- Cold HDD - throughput-oriented storage for data that is infrequently accessed | scenarios where the lowest storage cost is important

Throughput of HDD volumes is okay, but IOPS is extremely low!

## Instance Store
This is a volume that is physically attached to the host on which your instance is running. This is very good for quick IOPS (like caching or buffering), but it's not very reliable.  
If the hardware disk fails or your instance stops/hibernates/reboots, your data is lost. You can reboot your instance.  
An Instance Store is attached to an instance for the lifetime of an instance and can only be attached during the launch.

## Key Terminology
- **SAN** Storage Area Network - A network that allows devices (such as storage) to communicate over a network as if they had a physical connection.
- **NAS** Network-Attached Storage - Typically a server that has many storage disks attached to it that can be accessed by other computers over a network. 
- **RAID** Redundant array of independent disks - Typically used in a NAS. 

## Sources
- https://www.ibm.com/topics/storage-area-network
- https://stackoverflow.com/questions/15759571/iops-versus-throughput