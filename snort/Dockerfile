FROM glanf/base
MAINTAINER Simon Jouet

RUN apt-get update && apt-get install -y python snort supervisor

RUN mkdir /data
ADD logrunner.py /data/
ADD supervisord.conf /etc/supervisor/
ADD snort.conf /etc/snort/

ENTRYPOINT ifinit && /usr/bin/supervisord