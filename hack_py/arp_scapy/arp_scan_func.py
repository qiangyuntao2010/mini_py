#!/usr/bin/env python
# coding=utf-8


import logging
import sys
import os
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

def scapy_scan(dst_ip,queue=None):
    result_raw=srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(op=1,hwdst="00:00:00:00:00:00",pdst=dst_ip),timeout=1)
    print "result_raw",result_raw
    print result_raw[0]
    tmp_result=result_raw[0].res
    print "tmp_result",tmp_result
    arp_result=tmp_result[0][1].getlayer(ARP).fields['hwsrc']
    print "arp_result",arp_result
    if queue==None:
        print dst_ip,arp_result
    else:
        queue.put(dst_ip,arp_result)

if __name__=="__main__":
    scapy_scan(sys.argv[1])

