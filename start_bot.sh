#!/bin/bash

ETHERNET_INTERFACE='eno1'
SERVER_IP=$(/sbin/ifconfig $ETHERNET_INTERFACE | grep 'inet addr' | cut -d: -f2 | awk '{ print $1; }')

docker build -t hangoutsbot/hangoutsbot .
docker run -d -e HOST_IP=$SERVER_IP --network="bridge" -it --rm hangoutsbot/hangoutsbot
