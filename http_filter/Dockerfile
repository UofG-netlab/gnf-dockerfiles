# KW Dockerfile for Http_filter
FROM ubuntu
MAINTAINER Kyle White

RUN brctl addbr br0
RUN brctl addif br0 if1
RUN brctl addif br0 if2
RUN ip link set dev br0 up
RUN iptables -A FORWARD -j NFQUEUE -p tcp --destination-port 80 --queue-num 1
RUN python main.py

# INSTRUCTION arguments
