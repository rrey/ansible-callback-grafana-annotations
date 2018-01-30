#!/bin/bash

CONTAINER=$(docker ps | grep 'grafana/grafana'|awk '{print $1}')
[ -n "$CONTAINER" ] && echo "Container already running" && exit 0

docker pull grafana/grafana
[ $? -ne 0 ] && exit 1

docker run -d --name=grafana -p 3000:3000 grafana/grafana
sleep 2
exit $?
