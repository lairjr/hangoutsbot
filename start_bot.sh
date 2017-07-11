#!/bin/bash

ETHERNET_INTERFACE='en0'
SERVER_IP=$(/sbin/ifconfig $ETHERNET_INTERFACE | grep 'inet' | cut -d: -f2 | awk '{ print $2 }')

docker build -t hangoutsbot/hangoutsbot .
docker run -e HOST_IP=$SERVER_IP -it --rm hangoutsbot/hangoutsbot
