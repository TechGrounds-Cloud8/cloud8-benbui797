## Regions
The diagram in the request covered two regions, but there was no real use case (there were only 2 instances, 1 webserver and 1 admin server).   
After discussing with the product owner, I decided to start with 1 region with the option to expand when the needs arise.   
Due to the security policy, the admin server has to be in a different VPC than the webserver. In the drawing there are 4 public subnets, but I'll change this to 2, because we are using only 2 subnets. 
  
The region in which the servers should be launched are not specified, so for testing, we go with eu-central-1. The script is build to react to your settings of your AWS CLI.

## Instance Types and specifications
The instance types have not been defined in the requirements. Since it's only a single server, we assume the load isn't huge. Therefor we choose to work with the T3.micro from the free tier.
For the EBS storage, I have simply kept it at the default size of 8gb.

## Admin IP
The admin IP address (trusted IP) isn't specified. For testing, I have written a few lines of code that retrieves the IP address of the person that launched the stack. The stack will use this IP to grant SSH access to the admin server.

## Key pair
In the console, in your default region, create a new EC2 key pair called 'ec2-key-pair'. Both instances in the Stack will look for this key and use it to authenticate incoming SSH connections.
