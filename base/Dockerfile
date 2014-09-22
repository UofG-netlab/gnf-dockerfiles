# Implements wire functionality

FROM debian:wheezy
MAINTAINER Richard Cziva, Simon Jouet, Kyle White

RUN apt-get update && apt-get install -y \
	bridge-utils \
	net-tools \
	iptables 

ADD ifinit /usr/local/bin/
ADD brinit /usr/local/bin/
RUN chmod +x /usr/local/bin/ifinit
RUN chmod +x /usr/local/bin/brinit
ENTRYPOINT ifinit && /bin/bash
