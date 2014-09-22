# This is a simple HTTP Load Balancer

import nfqueue
from scapy.all import *
import os
os.system('iptables -A OUTPUT -p tcp --dport 80 -j NFQUEUE')

def callback(payload):
    data = payload.get_data()
    pkt = IP(data)
    if pkt.haslayer(DNSQR): # Beginning modifications
        pkt[IP].dst = '10.0.0.2'
        pkt[IP].len = len(str(pkt))
        pkt[UDP].len = len(str(pkt[UDP]))
        del pkt[IP].chksum
        payload.set_verdict_modified(nfqueue.NF_ACCEPT, str(pkt), len(pkt))

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

main()
