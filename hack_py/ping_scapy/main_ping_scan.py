#!/usr/bin/env python
# coding=utf-8
import time
from ping_scan_func import scan_ping_func
import ipaddress
import multiprocessing
import sys

def main_ping_scan():
    ping_dict={}
    all_net=ipaddress.ip_network(u'192.168.1.0/24',False)
    for tmp_net in all_net:
        net=str(tmp_net)
        ping_one=multiprocessing.Process(target=scan_ping_func,args=(net,))
        ping_one.start()
        ping_dict[net]=ping_one
    active_iplist=[]
    for ip,ip_process in ping_dict.items():
        if ip_process.exitcode==3:
            active_iplist.append(ip)
        else:
            ip_process.terminate()
    return sorted(active_iplist)

if __name__=="__main__":
    start=time.time()
    ip_list=main_ping_scan()
    end=time.time()
    for ip in ip_list:
        print ip
    print "Consume:",str(end-start)+"s"
