import requests

my_ip = requests.get('https://api.ipify.org').text

########################
### CONFIG VARIABLES ###
########################

# When true, S3 buckets, Backup Vaults etc will be deleted along with the stack.
TEST_ENV = True

# Add IP addresses as strings, seperated by comma's: [my_ip, "192.168.10.24", "10.0.15.156"]. Or add IPs in the parameter store for more security.
TRUSTED_IP = [my_ip]

# Name of keypair
KEY_PAIR = 'ec2-macbook-key' #'ec2-key-pair'

# Capacity settings for Auto-Scaling Group
MIN_CAPACITY = 1
MAX_CAPACITY = 3

if my_ip in TRUSTED_IP:
    print(f'Local IP found: {my_ip}')
    print('This IP has been added to the trusted IP addresses (allows SSH access to the Admin Server)')
