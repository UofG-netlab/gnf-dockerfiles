FROM ubuntu:14.04
MAINTAINER Simon Jouet

RUN apt-get update && \
	apt-get install -y openvswitch-switch curl

RUN curl -sSL https://get.docker.io/ubuntu/ | sudo sh
RUN echo "DOCKER_OPTS='-H tcp://0.0.0.0:4243 -H unix:///var/run/docker.sock --bip=192.168.1.1/24'" >> /etc/default/docker

RUN	cd /usr/local/bin/ && \
	curl -O https://raw.githubusercontent.com/jpetazzo/pipework/master/pipework && \
	chmod +x pipework

ADD glanf /usr/local/bin/
RUN chmod +x /usr/local/bin/glanf

CMD service docker start && service openvswitch-switch start && /bin/bash