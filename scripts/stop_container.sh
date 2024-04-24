#!/bin/bash
set -e

# Get the container IDs of running containers
containerids=$(docker ps -q)

# Check if any containers are running
if [ -n "$containerids" ]; then
    # Loop through each container ID
    for containerid in $containerids; do
        # Stop and remove the container
        docker rm -f "$containerid"
        echo "Container with ID $containerid stopped and removed."
    done
else
    echo "No running containers found."
fi
