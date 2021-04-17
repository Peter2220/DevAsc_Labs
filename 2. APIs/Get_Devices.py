import requests
from Get_Token import token

URL = 'https://sandboxdnac.cisco.com/api/v1/network-device'
hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
resp = requests.get(URL, headers=hdr)
device_list = resp.json()
print(device_list)