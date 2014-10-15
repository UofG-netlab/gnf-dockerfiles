# This is a simple DNS load balancer
# It resolves the domain name to random webservers

import nfqueue
from scapy.all import *
import os
import random

domain = os.environ.get('DOMAIN')
webservers_string = os.environ.get('WEBSERVERS')

if domain is None or webservers_string is None:
    print 'Env has not been set properly'
    sys.exit()

webservers = webservers_string.split() 

# implement your load balancing here
# this one is a random choice
def getwebserver():
    return random.choice(webservers)

def callback(payload):
    data = payload.get_data()
    pkt = IP(data)
    if not pkt.haslayer(DNSQR):
        payload.set_verdict(nfqueue.NF_ACCEPT)
    else:
        if domain in pkt[DNS].qd.qname:
            webserver = getwebserver()
            spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)/\
                          UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)/\
                          DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd,\
                          an=DNSRR(rrname=pkt[DNS].qd.qname, ttl=10, rdata=webserver))
            payload.set_verdict_modified(nfqueue.NF_ACCEPT, str(spoofed_pkt), len(spoofed_pkt))
            print 'Sent spoofed packet for domain %s - resolves for %s' % ( domain, webserver)

def main():
    q = nfqueue.queue()
    q.open()
    q.bind(socket.AF_INET)
    q.set_callback(callback)
    q.create_queue(0)
    try:
        q.try_run() # Main loop
    except KeyboardInterrupt:
        q.unbind(socket.AF_INET)
        q.close()
        os.system('iptables -F')
        os.system('iptables -X')
        sys.exit('Exiting')

# Set NFQUEUE
os.system('iptables -A FORWARD -p udp --dport 53 -j NFQUEUE')
main()
