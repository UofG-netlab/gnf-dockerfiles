FROM debian:wheezy
MAINTAINER Simon Jouet

RUN apt-get update && apt-get install -y \
	bridge-utils \
	tcpdump

ADD ifinit /usr/local/bin/
RUN chmod +x /usr/local/bin/ifinit