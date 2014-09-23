FROM glanf/base
MAINTAINER Simon Jouet

RUN apt-get update && apt-get install -y python snort

RUN mkdir /data
ADD logrunner.py /data/
ADD snort /etc/default/
ADD snort.conf /etc/snort/

ENTRYPOINT ifinit && \
	service snort start && \
	python /data/logrunner.py /var/log/snort/alert