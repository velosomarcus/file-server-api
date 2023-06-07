# How to build th image:
##  docker build --no-cache -t file-server-api:<tag> . -f ./docker/Dockerfile

# How to create and run the container:
##  docker run --name <file-server-api-container-name> -p 8888:8888 -d file-server-api:<tag>

FROM ubuntu:22.04

ARG TARGETPLATFORM
ARG BUILDPLATFORM
RUN echo "I am running on $BUILDPLATFORM, building for $TARGETPLATFORM"

SHELL ["/bin/bash", "-c"]

# Prevent dialog during apt install
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /workspace/file-server-api
COPY . /workspace/file-server-api

RUN apt-get clean && \
    apt-get update && \
    apt-get install -y \
    curl \
    net-tools \
    iputils-ping \
    wget \
    git \
    nano \
    build-essential \
    python3 \
    python3-pip

RUN cat /etc/os-release && \
    # install python dependencies \
    cd /workspace/file-server-api && \
    python3 -m pip install -r requirements.txt

EXPOSE 8888

# startup script
CMD cd /workspace/file-server-api && python3 main.py -p 8888
