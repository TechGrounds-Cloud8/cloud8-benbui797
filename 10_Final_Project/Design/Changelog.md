## Regions
The diagram in the request covered two regions, but there was no real use case (there were only 2 instances, 1 webserver and 1 admin server).   
After discussing with the product owner, I decided to start with 1 region with the option to expand when the needs arise.   
Due to the security policy, the admin server has to be in a different VPC than the webserver. In the drawing there are 4 public subnets, but I'll change this to 2 public and 2 private (because it's likely we'll need a private subnet in a future version).