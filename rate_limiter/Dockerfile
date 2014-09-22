FROM glanf/base
MAINTAINER Simon Jouet

ENV BITRATE 1mbps

ENTRYPOINT ifinit && brinit && \
	tc qdisc add dev if2 root handle 1: htb default 0xfffe && \
	tc class add dev if2 classid 1:0xffff parent 1: htb rate 1000000000 && \
	tc class add dev if2 classid 1:0xfffe parent 1:0xffff htb rate $BITRATE ceil $BITRATE && \
	tc qdisc add dev if1 root handle 1: htb default 0xfffe && \
	tc class add dev if1 classid 1:0xffff parent 1: htb rate 1000000000 && \
	tc class add dev if1 classid 1:0xfffe parent 1:0xffff htb rate $BITRATE ceil $BITRATE && \
	/bin/bash