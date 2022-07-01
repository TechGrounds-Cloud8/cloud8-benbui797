## Regions
The diagram in the request covered two regions, but there was no real use case (there were only 2 instances, 1 webserver and 1 admin server).   
After discussing with the product owner, I decided to start with 1 region with the option to expand when the needs arise.   
Due to the security policy, the admin server has to be in a different VPC than the webserver. In the drawing there are 4 public subnets, but I'll change this to 2 public and 2 private (because it's likely we'll need a private subnet in a future version).  
  
The region in which the servers should be launched are not specified, so for testing, we go with eu-central-1. The script is build to react to your settings of your AWS CLI.

## Availability Zones
The current diagram asks for 2 AZ subnets, but I have changed this to 3 (max in eu-central-1). In the future, we might want to raise the availability of the service and for that, we'll need the subnets to cover as many AZ's as possible. 

## Instance Types
The instance types have not been defined in the requirements. Since it's only a single server, we assume the load isn't huge. Therefor we choose to work with the T3.micro from the free tier.
