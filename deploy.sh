#!/bin/bash

docker build -t neo-transcriber:1.0 .

docker run -dti -p 8000:8000 --mount type=bind,src=/root/neo-transcriber,dst=/data neo-transcriber:1.0