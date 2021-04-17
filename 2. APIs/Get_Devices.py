import requests
from pprint import pprint
from Get_Token import token

URL = 'https://sandboxdnac.cisco.com/api/v1/network-device'
hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
resp = requests.get(URL, headers=hdr)
device_list = resp.json()

# Write the output to a file
with open('Device_list.json', 'wt') as out:
    pprint(device_list, stream=out)

pprint(device_list)