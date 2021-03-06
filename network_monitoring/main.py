
import requests
import time, threading
import subprocess
import os
from subprocess import Popen

delta = float(os.environ.get('DELTA'))

if delta is None:
    print 'Env has not been set properly'
    sys.exit()

url = 'http://172.17.42.1:8081/notification'

def stat():
        threading.Timer(delta, stat).start()
        p = Popen(["netstat", "-i"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        x = out.split('\n')
        inbytes = x[4].split()[3]
        outbytes = x[5].split()[3]
        notif = "InBytes = " +  inbytes + ", OutBytes" + outbytes
        requests.post(url, data=notif)


stat()

