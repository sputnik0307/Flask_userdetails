#!/bin/bash
set -e

#pull the docker image from docker hub
docker pull sputnik03/user-details-app-codebuild

#run the docker image as a container
docker run -d -p 3000:3000 sputnik03/user-details-app-codebuild

