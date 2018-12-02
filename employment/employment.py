#!/usr/bin/env python
# coding=utf-8
import os
import argparse
_read_file="./employee.txt"
os.system("pwd")
lines=[]



def search(tmp_list):
    #user_input=raw_input("\033[0;0;32mplease input the hint info: \033[0m").strip()
    read_file=open(_read_file,"r+")
    lines=read_file.readlines()
    tmp_line=""
    for line in lines:
        if tmp_list in line and len(tmp_list)!=0:
            tmp_line=line
            print "\033[0;0;32mInformation: \033[0m",tmp_line
    if len(tmp_line)==0:
        print "\033[0;0;31mNo info!\033[0m"

def insert(tmp_list):
    read_file=open(_read_file,"r+")
    lines=read_file.readlines()
    while True:
        #tmp_list=raw_input("\033[0;0;32mPlease input the info:(format)[name] [position] [age]: \033[0m")
        if len(tmp_list.split(" "))!=3:
            print "\033[0;0;31mNumber of arguments false\033[0m"
            continue
        if tmp_list.split(" ")[0].isalpha() and tmp_list.split(" ")[1].isalpha() and tmp_list.split(" ")[2].isdigit():pass
        else:
            print "\033[0;0;31mformat error \033[0m"
            continue
        if tmp_list.split(" ")[0].strip() in lines:
            print "\033[0;0;31mRepeated name\033[0m"
            continue
        read_file.write("%s\n"%(tmp_list))
        read_file.flush()
        break
    read_file.close()
    
def delete(tmp_list):
    read_file=open(_read_file,"r+")
    lines=read_file.readlines()
    while True:
        #tmp_list=raw_input("\033[0;0;32mPlease input the name you want to delete:\033[0m").strip()
        match=len(lines)
        for line in lines:
            if tmp_list in line:
                lines.remove(line)
                break
        if match==len(lines):
            print "\033[0;0;31mInvalid name\033[0m"
            continue
        print lines
        read_file.close()
        os.system("rm -f test")
        new_file=open("employee.txt","w")
        for i in lines:
            new_file.write(i)
        read_file.close()
        break

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    #Operations
    parser.add_argument("--search",type=str,default='',metavar='name',help='the name you want to search')
    parser.add_argument("--delete",type=str,default='',metavar='name',help='the name you want to delete')
    parser.add_argument("--insert",type=str,default='',metavar='name position age',help="you need to input the detail info")
    args=parser.parse_args()
    
    search_name=args.search
    delete_name=args.delete
    add_info=args.insert
    
    if search_name:
        search(search_name)

    if delete_name:
        delete(delete_name)

    if add_info:
        insert(add_info)




