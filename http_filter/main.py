from netfilterqueue import NetfilterQueue
from scapy.all import *
import requests

def callback(pkt):
        parsed = pkt.get_payload()
        print parsed.encode('hex')

        if 'hack' in parsed:
            pkt.drop()
            print "packet dropped"
            requests.post(url, data="Http Filtered content")	
        else:
            pkt.accept()


nfqueue = NetfilterQueue()
nfqueue.bind(1, callback)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print


