FROM glanf/base
MAINTAINER Richard Cziva

RUN apt-get install -y \
    python \ 
    scapy \
    python-nfqueue \
    build-essential \
    python-dev \
    libnetfilter-queue-dev \
    python-pip

RUN pip install netfilterqueue

ADD loadbalancer.py .

ENTRYPOINT ifinit && brinit && python loadbalancer.py
