# snap store update
    snap-store --quit && sudo snap refresh snap-store

# docker setup
## Add Docker's official GPG key:
    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc

## Add the repository to Apt sources:
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update

## install latest version
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    sudo apt install docker-compose

## check docker service
    sudo systemctl status docker

## add docker to user
    sudo groupadd docker
    sudo usermod -aG docker $USER
    newgrp docker

# docker usage
    docker run hello-world

    docker pull ubuntu
    docker run -it ubuntu

    docker ps -a # view all containers

    docker rm container_name

    docker run -it --name ubuntu --volume test:/mnt ubuntu

    echo test > /mnt/test

    docker volume ls
    sudo cat /var/lib/docker/volumes/test/_data/test

    docker volume remove test
    docker container prune

    docker run -it --name ubuntu --volume /home/user:/mnt ubuntu

    *** TODO figure docker root user for files issue

## docker network

    docker run -p 8080:80 nginx

    docker run --net=host nginx # works on just localhost

## docker-compose

    docker-compose up -d

    docker-compose logs

    docker-compose down

    docker stop container_name
    docker kill container_name

## docker build

    docker build -t iris-docker .

    docker run -p 9999:9999 iris-docker

## docker exec

    docker run -it python:3.9
    docker container start reverent_tharp 
    docker exec -it reverent_tharp sh
    docker container prune

    

