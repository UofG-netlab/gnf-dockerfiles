import time
import sys
import os
import httplib

def postNotification(notification):
	conn = httplib.HTTPConnection("172.17.42.1:8081")
	conn.request("POST", "/notification", notification)
	conn.close()

def tail(file):
	interval = 1.0
	while True:
		cursor = file.tell()
		line = file.readline()
		if not line:
			time.sleep(interval)
			file.seek(cursor)
		else:
			yield line

print 'logrunner is running ...'
with open(sys.argv[1]) as f:
	chunk = []
	for line in tail(f):
		if line != os.linesep:
			chunk.append(line)
		else:
			alert = ''.join(chunk)
			print alert
			postNotification(alert)
			chunk = []
