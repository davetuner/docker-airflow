#!/bin/bash

set -e

TAG=1.10.0

build() {
    NAME=$1
    IMAGE=transformersreg11.azurecr.io/$NAME:$TAG
    # cd $([ -z "$2" ] && echo "./$NAME" || echo "$2")
    echo '--------------------------' building $IMAGE in $(pwd)
    docker build -t $IMAGE .
    cd -
}

build airflow
# build master
# build worker
# build submit
#build java-template template/java
#build python-template template/scala
#build python-template template/python
