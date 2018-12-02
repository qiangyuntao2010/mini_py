#!/usr/bin/env python
# coding=utf-8
from scapy.all import *
from random import randint
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def scan_ping_func(host):
    a=2**16
    id_ip=randint(0,a)
    id_icmp=randint(0,a)
    seq_packet=randint(0,a)
    Packet=IP(dst=host,ttl=128,id=id_ip)/ICMP(id=id_icmp,seq=seq_packet)/b'qyt2010'
    ping_packet=sr1(Packet,timeout=2,verbose=False)
    if ping_packet:
        #ping_packet.show()
        os._exit(3)

if __name__=='__main__':
    scan_ping_func(sys.argv[1])

