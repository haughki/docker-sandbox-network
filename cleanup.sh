#!/usr/bin/env bash

docker stop host_0_02
docker rm host_0_02
docker rmi host_0_02

docker stop host_100_02
docker rm host_100_02
docker rmi host_100_02

docker stop router_00
docker rm router_00
docker rmi router_00