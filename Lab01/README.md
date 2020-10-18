# Cowsay in docker

Create a container which prints an ASCII picture of a cow with a random message using the 
[fortune](https://en.wikipedia.org/wiki/Fortune_(Unix)) and the [cowsay](https://en.wikipedia.org/wiki/Cowsay) packages.

The command to use: `fortune | cowsay`
```
 ______________________________________
/ Q: How many Martians does it take to \
| screw in a light bulb? A: One and a  |
\ half.                                /
 --------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```
Steps:
  * Create a `Dockerfile` which meets the requirements
  * Build a docker image using the created `Dockerfile`
  * Create a container with the built image and run it

## Build
Chose the directory of the desired distribution (*alpine/ubuntu*), there is a `Dockerfile` in each.

Make sure you are in the root of the chosen directory and the `Dockerfile` is there.

Build the docker image with this command:
```
docker build -t cowsay_img .
```
*Explanation of the command: the `-t cowsay_img` is the name of the built image and the `.` is the path of the `Dockerfile`.*
*More detailed usage: [official docs](https://docs.docker.com/engine/reference/commandline/build/)*

## Run
To run the docker container from the image you created, run this command:
```
docker run cowsay_img
```
*Explanation of the command: the `cowsay_img` is the name of the image from which we would like to create our container.*
*More detailed usage: [official docs](https://docs.docker.com/engine/reference/commandline/run/)*
