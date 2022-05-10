# NTW-06 Subnetting
An IP address consists of a network- and a host (device) portion. Without Submasking, we would not be able to distinquish between the two.  

Every bit that is a 1 in a subnet mask, belongs to the network. So for 255.255.255.0, that means all bits in the first 3 bytes belong to the network. You can layer this with the bits in the IP address and perform bitwise AND and know the values of the network.  

When you perform the bitwise AND, only the bits which are 1 in both sequences will be a 1 in the resulting sequence.  

**Why is an address split up in two parts?**
When one hosts wants to communicate with another, it sends out a Broadcast to identify the receiver. The receiving host will reply with it's details. But every other host in the network will also receive the broadcast. A lot of hosts sending out broadcasts at the same time will clutter the network. Therefore the network is split up into smaller pieces. A Router is a physical border between networks and broadcasts do not cross a router, instead the router intelligently routes the request.   

**Submasking**  
Submasking is done by changing the default subnet mask by borrowing some bits from the host portion of the address.  
  
Some basic bitwise operation understanding is required. If you move all bits left, you double the value (provided you are not at the end of your byte...). Moving all bits 1 step right, you divide it by 2.  
By borrowing a bit from the host portion, you double the amount of networks and divide the amount of hosts by 2. If you borrow another bit, it's again *2 and /2. 

Default submasks are divided into classes, because you are limited how many subnet you can make based on masking.  

Class A: starts with 1-126.x.x.x - default mask = 255.0.0.0 = +- 16 million host addresses (an ISP might use this)
Class B: starts with 128-191.x.x.x - default mask = 255.255.0.0 = +- 65K host addresses (a big company might use this)
Class C: starts with 192-223.x.x.x - default mask = 255.255.255.0 = 256 host addresses (normal connections)


## Key terminology
- CIDR: Classless Inter-Domain Routing (slash notation). The number after the slash describes the length of the network mask in bits. /24 == 24 bits == 3 bytes == 255.255.255.0
- Broadcast address: The address on which the broadcast signal is transmitted (and connects the local network to the outside)

## Exercise
### Sources
- https://www.ipxo.com/tutorial/what-is-subnet-mask/
- https://www.youtube.com/watch?v=s_Ntt6eTn94
- https://www.ipxo.com/subnet-cheat-sheet/
- https://en.wikipedia.org/wiki/Broadcast_address
- https://cloud.in28minutes.com/aws-certification-public-subnet-vs-private-subnet

### Overcome challenges
- Understanding Subnetting
- Understanding Subnet masks
- Difference between private and public subnets


### Results

Design a networkarchitecture that meets the following demands:
- 1 private subnet with atleast 15 hosts. Only accessable within the LAN.
- 1 private subnet with atleast 30 hosts (excluding NAT gateway). This network should have internet access.
- 1 public subnet with a internet gateway. This subnet needs to be able to place atleast 5 hosts (excluding the internet gateway)



