# PING-PONG


## Setting up the environment

### Build
Build the docker image with this command:
```
docker build -t ping-pong-alpine:v1 src
```
### Network
Create the network with this command:
```
docker network create ping-pong-network 
```

### Volume
Create the volume with this command:
```
docker volume create ping-pong-volume
```

## Run
### Server
Start the server with this command:
```
docker run --net ping-pong-network -itd --name ping-pong-server -v ping-pong-volume:/tmp ping-pong-alpine:v1 python ./server.py ping-pong-server
```
### Client
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
Change the current directory to the Mountpoint of the volume:
*Mind that superuser rights are required for this action*
```
sudo su
cd /var/lib/docker/volumes/ping-pong-volume/_data
cat ping-pong.log
```
If the every PING followed by a PONG (like in the output below) that means that everything works :)

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