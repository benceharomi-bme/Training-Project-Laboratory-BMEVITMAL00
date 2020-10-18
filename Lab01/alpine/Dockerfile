FROM nginx:alpine
RUN apk update && \
    apk add fortune && \
    apk add --no-cache git perl && \
    cd /tmp && \
    git clone https://github.com/jasonm23/cowsay.git  && \
    cd cowsay ; ./install.sh /usr/local && \
    rm -rf /var/cache/apk/* /var/tmp/* /tmp/* && \
    apk del git
CMD /usr/bin/fortune | /usr/local/bin/cowsay

