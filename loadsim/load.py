#!/usr/bin/env python

import nfqueue
import signal
import socket
import os

expense = float(os.getenv("LOAD_FACTOR", "5.0"))
limit = int(expense * (2 ** expense))

def cb(payload):
    sum = 0
    for a in xrange(1, limit):
        sum += 1


if __name__ == "__main__":
    def inthandler(signum, frame):
        """Handle an interrupt"""
        print("Exiting...")
        q.unbind(socket.AF_INET)
        q.close()

    # Register signal handler
    signal.signal(signal.SIGINT, inthandler)
    signal.signal(signal.SIGTERM, inthandler)

    q = None
    q = nfqueue.queue()
    q.open()
    q.bind(socket.AF_INET)
    q.set_callback(cb)
    q.create_queue(0)

    q.try_run()

