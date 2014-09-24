# Allow HTTP traffic only
# Firewall example for GLANF

FROM glanf/base
MAINTAINER Richard Cziva

ENTRYPOINT ifinit && \
        brinit && \
        iptables -A FORWARD -p tcp --dport 80 -j ACCEPT && \
        iptables -A FORWARD -j DROP && \
        /bin/bash
