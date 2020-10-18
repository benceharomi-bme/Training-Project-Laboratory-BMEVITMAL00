# PING-PONG
Create a network with 2 connected containers (*server* and *client*) which send *PING* and *PONG* messages to each other.
Ensure persistent storage of the logs.

Tasks:
  * create a `Dockerfile` and build a docker image which contains the python resource files (`server.py` and `client.py`)
  * setting up a docker network for the containers
  * creating a volume to save the logs (both the client and the server logs can be found in this path: `/tmp/ping-pong.log`)
  * starting the containers and checking the logs to check if everything works the way it should

## Setting up the environment
Building the image and creating the network and the volume.

Build the docker image with this command:
```
docker build -t ping-pong-alpine:v1 src
```
Create the network with this command:
```
docker network create ping-pong-network 
```
Create the volume with this command:
```
docker volume create ping-pong-volume
```

## Run
Starting the server and the client:
Start the server with this command:
```
docker run --net ping-pong-network -itd --name ping-pong-server -v ping-pong-volume:/tmp ping-pong-alpine:v1 python ./server.py ping-pong-server
```
Start the client with this command:
```
docker run --net ping-pong-network -itd --name ping-pong-client -v ping-pong-volume:/tmp ping-pong-alpine:v1 python ./client.py ping-pong-server
```

## Result
Look the content of the `ping-pong.log` file to check if everything works the way it should.
Inspect the volume:
```
docker inspect ping-pong-volume
```
output:
```
[
    {
        "CreatedAt": "2020-10-18T17:01:45+02:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/ping-pong-volume/_data",
        "Name": "ping-pong-volume",
        "Options": {},
        "Scope": "local"
    }
]
```
Change the current directory to the Mountpoint of the volume *(Please mind that superuser rights are required for this action)*:
```
sudo su
cd /var/lib/docker/volumes/ping-pong-volume/_data
cat ping-pong.log
```
If every PING followed by a PONG (like in the output below) that means that everything works :)

output:
```
2020-10-18 15:11:46 : PING
2020-10-18 15:11:46  : PONG
2020-10-18 15:11:47 : PING
2020-10-18 15:11:47  : PONG
2020-10-18 15:11:48 : PING
2020-10-18 15:11:48  : PONG
2020-10-18 15:11:49 : PING
2020-10-18 15:11:49  : PONG
2020-10-18 15:11:50 : PING
2020-10-18 15:11:50  : PONG
```
