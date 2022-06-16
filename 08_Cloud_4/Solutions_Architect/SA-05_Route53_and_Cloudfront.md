# Route53
[Route 53](../../06_Cloud_2/AWS-13-3_Route53.md)

# CloudFront
[CloudFront](../../06_Cloud_2/AWS-13-2_CloudFront.md)  

- **Signed URL** Allow you to specify beginning and expiration date/time and IP addresses/ranges of users. It's for *Individual files* and for devices that don't support cookies. 
- **Signed Cookies** Signed ookies allow you to control who can access your content when you don't want to change your current URLs or when you want to provide access to multiple restricted files, for example, all of the files in the subscribers' area of a website. You can use Signed Cookies for *multiple files*. 
  

## Cache and Behaviour Settings
- **TTL** Time To Live - This is defined at the **Behaviour Level**.
- You can define a maximum TTL and a default TTL.
- You can define different TTLs for different file types.
- After expiration, CloudFront checks the origin for any new requests (checks if the file is the latest version)
- Headers can be used to control the cache:
  - `Cache-Control max-age=(seconds)` - Specify how long before CloudFront gets the object again from the Origin
  - `Expires` - Specify an expiration date and time
  
- You can configure CloudFront to forward **headers** in the viewer request to the origin. 
- CloudFront can cache multiple versions of an object based on the values in one or more request headers
- Controlled in a behaviour to do one of the following:
  - Forward all headers to your origin (objects are not cached)
  - Forward a whitelist of headers that you specify
  - Forward only the default headers (doesn't cache objects based on values in the request headers)

https://www.tutorialspoint.com/requests/requests_http_requests_headers.htm

## CloudFront Origin Access Identity (OAI)
Special user account (principal) that CloudFront uses to retrieve data from the Origin (S3). You have to configure your bucket policy to allow access from the specific OAI. It will block access from users accessing the S3 link directly.  
  
EC2 origins do not support OAI. Instead you can add a list of CloudFront Nodes IP addresses to the Origins security group.  
  
## CloudFront SSL/TLS Certification
- You can use a certificate from AWS Certificate Manager or third-party CA. If it's AWS CM, it must be issued in *us-east-1*.
- You can change the default domain name (*.cloudfront.aws) to your custom domainname using CNAMES.
- S3 already has it's own certificate that you cannot change 
  
**CloudFront Server Name Indication (SNI)**
You can have multiple certificates share the same IP address. CloudFront will route it to the corresponding server according to the request header (it matches the domain name in the header to the corresponding server)

## Lambda@Edge
- Run Node.js and Python lambda functions to customize the content CloudFront delivers
- It executes the functions closer to the viewer (thus reducing latency)
- Can be run at the following points:
  - *Viewer Request* - CloudFront receives a request from a viewer
  - *Origin Request* - Before CloudFront forwards the request to the origin
  - *Origin Response* - After CloudFront receives the response from the origin
  - *Viewer Response* - Before CloudFront forwards the response to the viewer

- **Anycast** Connect multiple hosts/servers to a single IP address

# Todo
- Global Accelerator IP https://d1.awsstatic.com/Networking/AGA-Multi-Region-Usecase-2000px.39194f2f7dd49fca26217836d10d522298c1abcc.png
  
https://mxx.news/media/posts/1/responsive/Multi-regional-setup-with-Cloudfront-md.png.mxx.webp
  
https://d2908q01vomqb2.cloudfront.net/fc074d501302eb2b93e2554793fcaf50b3bf7291/2020/07/15/Optimizing-application-performance-with-Accelerated-VPN-connections-2.png