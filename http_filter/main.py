from netfilterqueue import NetfilterQueue
from scapy.all import *

def callback(pkt):
        parsed = pkt.get_payload()
        print parsed.encode('hex')

        if 'hack' in parsed:
                pkt.drop()
        else:
                pkt.accept()


nfqueue = NetfilterQueue()
nfqueue.bind(1, callback)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print


