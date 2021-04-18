#!/usr/bin/bash
read -s -p "Enter the token: " ENTER_TOKEN_HERE

curl -X GET \
 -H 'Content-Type: application/json' \
 -H 'X-Auth-Token: '$ENTER_TOKEN_HERE'' \
 https://sandboxdnac.cisco.com/api/v1/network-device
