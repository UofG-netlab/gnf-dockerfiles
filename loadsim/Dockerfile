FROM glanf/base
MAINTAINER James Guthrie

RUN apt-get update && apt-get install -y \
            python-nfqueue

ADD load.py /usr/local/sbin/
RUN chmod +x /usr/local/sbin/load.py

ENV DELAY 1ms
ENV LOAD_FACTOR 5.0

ENTRYPOINT ifinit && \
           brinit && \
           tc qdisc add dev if1 root netem delay $DELAY && \
           tc qdisc add dev if2 root netem delay $DELAY && \
           iptables -A FORWARD -j NFQUEUE && \
           exec /usr/local/sbin/load.py
