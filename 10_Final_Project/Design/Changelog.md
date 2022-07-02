## Regions
The diagram in the request covered two regions, but there was no real use case (there were only 2 instances, 1 webserver and 1 admin server).   
After discussing with the product owner, I decided to start with 1 region with the option to expand when the needs arise.   
Due to the security policy, the admin server has to be in a different VPC than the webserver. In the drawing there are 4 public subnets, but I'll change this to 2, because we are using only 2 subnets. 
  
The region in which the servers should be launched are not specified, so for testing, we go with eu-central-1. The script is build to react to your settings of your AWS CLI.

## Instance Types
The instance types have not been defined in the requirements. Since it's only a single server, we assume the load isn't huge. Therefor we choose to work with the T3.micro from the free tier.
