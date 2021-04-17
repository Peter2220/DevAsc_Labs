#!/usr/bin/bash
read -s -p "Username: " USERNAME
echo " "
read -s -p "Password: " PASSWORD
echo " "
echo " "

curl -X POST \
 -u ''$(echo $USERNAME:$PASSWORD)'' \
 -H 'Content-Type: application/json' \
 https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token