# Requirements
- WebServer should not have a public IP and should be accessable through a proxy (load balancer)
- If a customer connects to the load balancer via HTTP, it should be upgraded to HTTPS automatically
- The HTTPS connection should use TLS 1.2 or higher
- The loadbalancer should perform health checks on the web server
- If a healthcheck fails, the server should automatically be restored
- If the webserver has a high load, additional web servers should launch. The client thinks a maximum of 3 servers are enough.

# Design
The main change is that we'll add a loadbalancer. The loadbalancer can statisfy most of the requirements, but we'll need a few additional services.

- We create private subnets in the same VPC as the web server currently is. **We'll create 3 subnets so we can spread the servers over 3 AZ's**
- We'll place the ELB (ALB) in the public subnet (it'll replace the webserver)
- We'll create an Auto-Scaling Group that covers the private subnets and has a maximum of 3 webservers.
- Create AMI from snapshot of current WebServer?
- We'll configure the ELB to perform healthchecks and automatically replace an unhealthy server
- The load balancer should change HTTP to HTTPS connections (with TLS 1.2 or higher) - Need to install a certificate on the servers
- Update the NACL and SG's so we can SSH connect to the WebServers in the private subnet via the AdminServer.


# Services
- Elastic Load Balancer (Application Load Balancer)
- EC2 Auto-scaling group 
- Configuring Health Checks on the ELB
- Certificate Manager
