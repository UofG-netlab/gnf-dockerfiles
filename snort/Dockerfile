FROM glanf/base
MAINTAINER Simon Jouet

RUN apt-get update && apt-get install -y python snort

RUN mkdir /data
ADD logrunner.py /data/
ADD snort /etc/default/
ADD snort.conf /etc/snort/

#ENTRYPOINT ifinit && \
#	snort -D -Q -c /etc/snort/snort.conf -i if1:if2 --daq afpacket --daq-mode inline --daq-var buffer_size_mb=$BUFSIZE && \
#	#python /data/logrunner.py /var/log/snort/alert