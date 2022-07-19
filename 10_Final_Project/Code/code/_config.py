import requests

my_ip = requests.get('https://api.ipify.org').text

########################
### CONFIG VARIABLES ###
########################

# When true, S3 buckets, Backup Vaults etc will be deleted along with the stack.
TEST_ENV = True

# Add IP addresses as strings, seperated by comma's: [my_ip, "192.168.10.24", "10.0.15.156"]
TRUSTED_IP = [my_ip]

AVAILABILITY_ZONES = ['eu-central-1a', 'eu-central-1b', 'eu-central-1c']

if my_ip in TRUSTED_IP:
    print(f'Local IP found: {my_ip}')
    print('This IP has been added to the trusted IP addresses (allows SSH access to the Admin Server)')
