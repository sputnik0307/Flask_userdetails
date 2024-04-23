#!/bin/bash
set -e

#pull the docker image from docker hub
docker pull sputnik03/simple-python-flask-app

#run the docker image as a container
docker run -d -p 5000:5000 sputnik03/simple-python-flask-app
