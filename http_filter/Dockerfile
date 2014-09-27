FROM glanf/base
MAINTAINER Kyle White

RUN apt-get install -y \
    python \ 
    scapy \
    tcpdump \
    python-nfqueue \
    build-essential \
    python-dev \
    libnetfilter-queue-dev \
    python-pip

RUN pip install netfilterqueue
RUN pip install requests

RUN mkdir data
ADD main.py ./data/
RUN chmod +x ./data/main.py

ENTRYPOINT ifinit && \
	brinit && \
	iptables -A FORWARD -j NFQUEUE -p tcp --destination-port 80 --queue-num 1 && \
	python ./data/main.py
