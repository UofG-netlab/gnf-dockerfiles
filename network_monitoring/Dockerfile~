
import requests
import time, threading
import subprocess
from subprocess import Popen

delta = os.environ.get('DELTA')

url = 'http://172.17.42.1:8081/notification'

def stat():
        threading.Timer(delta, stat).start()
        p = Popen(["netstat", "-i"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        x = out.split('\n')
        inbytes = x[4].split()[3]
        outbytes = x[5].split()[3]
        notif = "inbytes = " +  inbytes + ", Outbytes" + outbytes
        requests.post(url, data=notif)


stat()

