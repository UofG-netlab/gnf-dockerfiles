# KW Dockerfile for Http_filter
FROM ubuntu
MAINTAINER Kyle White


ENTRYPOINT ifinit &&
	 brctl addbr br0 &&
	 brctl addif br0 if1 &&
	 brctl addif br0 if2 &&
	 ip link set dev br0 up &&
	 iptables -A FORWARD -j NFQUEUE -p tcp --destination-port 80 --queue-num 1 &&
	 python main.py
