#!/bin/bash

docker build -t rick_roll .
docker run -d --restart unless-stopped --name rick_roll -p 4100:4100 rick_roll