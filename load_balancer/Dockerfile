# A wee DNS load balancer for GLANF

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

# Set your domain and webservers here!
ENV DOMAIN testwebpage
ENV WEBSERVERS 10.0.0.1 10.0.0.3

ENTRYPOINT ifinit && \
        brinit && \
        python ./data/loadbalancer.py
