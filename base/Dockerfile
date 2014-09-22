# Implements wire functionality

FROM debian:wheezy
MAINTAINER Richard Cziva, Simon Jouet, Kyle White

RUN apt-get update && apt-get install -y \
	bridge-utils \
	net-tools \
	iptables 

ADD ifinit /usr/local/bin/
RUN chmod +x /usr/local/bin/ifinit
ENTRYPOINT ifinit && brctl addbr br0 && brctl addif br0 if1 && brctl addif br0 if2 && ifconfig dev br0 up && /bin/bash
