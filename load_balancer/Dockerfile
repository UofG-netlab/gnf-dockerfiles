FROM glanf/base
MAINTAINER Richard Cziva

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

RUN mkdir data
ADD loadbalancer.py ./data/
RUN chmod +x ./data/loadbalancer.py

ENTRYPOINT ifinit && \
        brinit && \
        python ./data/loadbalancer.py
