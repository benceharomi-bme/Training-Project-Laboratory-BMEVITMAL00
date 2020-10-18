FROM ubuntu:latest
RUN apt update && \
    apt install -y fortune && \
    apt install -y cowsay
CMD /usr/games/fortune | /usr/games/cowsay

