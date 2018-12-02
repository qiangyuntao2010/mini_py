#!/usr/bin/env python
# coding=utf-8
import time
from arp_scan_func import scapy_scan
import ipaddress
import multiprocessing
import sys
import Queue

arp_dict={}
def main_ping_scan():
    arp_queue=Queue.Queue()
    all_net=ipaddress.ip_network(u'192.168.0.105',False)
    for tmp_net in all_net:
        net=str(tmp_net)
        arp_one=multiprocessing.Process(target=scapy_scan,args=(net,arp_queue))
        arp_one.start()
    time.sleep(2)
    while True:
        if arp_queue.empty() is True:
            break
        else:
            ip,mac=arp_queue.get()
            arp_dict[ip]=mac

if __name__=="__main__":
    start=time.time()
    ip_list=main_ping_scan()
    end=time.time()
    for ip,mac in arp_dict:
        print ip,mac
    print "Consume:",str(end-start)+"s"
