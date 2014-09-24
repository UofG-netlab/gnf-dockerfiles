# Proof of concept for Network Monitoring Container

FROM glanf/base
MAINTAINER Kyle White

RUN apt-get install -y \
    python \ 
    build-essential \
    python-dev \
    python-pip

RUN pip install requests

RUN mkdir data
ADD main.py ./data/
RUN chmod +x ./data/main.py

# Set delta for notification of stats here (float, seconds)
ENV DELTA 60.0

ENTRYPOINT ifinit && \
        brinit && \
        python ./data/main.py
