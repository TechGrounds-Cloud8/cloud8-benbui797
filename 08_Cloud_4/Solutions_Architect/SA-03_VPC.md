# VPC

## VPC Endpoints
Endpoints are used to connect to public AWS services with private IP addresses.

**Types of VPC Endpoints:**
- **Interface** An Interface Endpoint sends traffic to the endpoint services that uses a Network Load Balancer to distribute traffic. Traffic destined for the endpoint service is resolved using DNS.
- **GatewayLoadBalancer** A GatewayLoadBalancer sends traffic to a fleet of virtual appliances using private IP addresses. You route traffic from your VPC to your GWLB endpoint using route tables. The GWLB distributes traffic to the virtual appliances and can scale with demand.
- **Gateway** A Gateway Endpoint sends traffic to AWS S3 or DynomoDB using private IP addresses. You route the traffic from your VPC to the Gateway Endpoint using route tables. Gateway Endpoints do not enable AWS PrivateLink.

## VPN
### Client VPN
Add a VPN Endpoint to your VPC. You can connect your subnets to this endpoint.  
Install a VPN client locally and then update the route tables. The VPN Client uses SSL/TLS (port 443) to connect, so the data is encryped.

### Site-to-Site VPN
Deploy a Virtual Private Gateway (VPG) in the VPC and a Customer Gateway in a local datacenter to connect your local network to the VPC.

### AWS Direct Connect (DX)
Physically connect your local datacenter to AWS by connecting to a Direct Connect Center. From there, traffic is routed over the AWS backbone network. It can achieve speeds from 1/10 Gbps (100 Gbps is also available in some locations). Lower speeds from 50Mbps to 500Mbps can be accessed via a APN partner.  
  
**DX connections are NOT encrypted!!** If you want this, you need to establish a IPSec S2S VPN connection to add encryption in transit.

- **VIF** Virtual Interface - Transit VIF to connect a DXGW to a Transit GW. Private to connect to your VPC. Public to allow connection to AWS Public Services (S3, CloudFront and DynamoDB). This is the connection point from the DX location into the cloud.
- **VGW** Virtual Gateway - put these in your VPC to connect DX to your VPC.
- **BGP ASN**  Border Gateway Protocol Autonomous System Number
- **DX Gateway** Allows to connect to multiple AWS Regions via the DX network.
- **Egress Only Gateway** Outbound only internet gateway. To be used by IPv6 addresses, because they don't use private IPs/NAT.

### Border Gateway Protocol (BGP)
Border Gateway Protocol (BGP) is a set of rules and procedures that help an autonomous system (AS) exchange routing information over the internet. An AS is a network of computers run by an entity, e.g., a university or a large corporation, controlling a range of IP addresses.  
  
Every AS manages a table containing all of its known routes to other networks, which is then propagated to neighboring networks (a.k.a., peers). The BGP decision-making mechanism analyzes the data and selects the best route for the next network hop.  
  
BGP is the basis for the transfer of data between locations over the internet. It can also be used to manage routing within large networks, such as ISPs, layer 3 VPN services, IP telephony, large-scale web caching, or as a way to improve network stability.  
  
- https://www.imperva.com/learn/ddos/border-gateway-protocol-bgp/  
- https://ip-noc.com/bgp-asn-intro/

### Digital Cloud Summary
- https://digitalcloud.training/amazon-vpc/
- https://digitalcloud.training/aws-direct-connect/

# Todo
- Peering 2 VPC networks (set up ICMP + TCP in SG. Add peering ID to route table)
- VPC Endpoint configuration
- Client VPN vs Site2Site VPN?

