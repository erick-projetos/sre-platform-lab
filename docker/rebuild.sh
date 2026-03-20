#!/bin/bash
docker-compose down -v
docker-compose up -d --build
wait 1s
docker ps -a
