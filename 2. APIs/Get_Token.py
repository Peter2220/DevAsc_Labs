import requests
from getpass import getpass

URL = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
username = getpass("Username: ")
password =  getpass("Password: ")
r = requests.post(URL, auth=(username, password))

print(" ")
print("Status code: " + str(r.status_code), end="\n\n")
token = r.json()["Token"]
#print("Token: " + "\n\n" + token, end="\n\n")