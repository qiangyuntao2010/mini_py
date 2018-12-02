#!/usr/bin/env python
# coding=utf-8
import os
import shutil

path=os.path.join(os.getcwd(),"test")

def create_folder(path_name):
    if not os.path.exists(path_name):
        os.mkdir(path_name)
    else:
        pass

def move_file(old,new):
    if os.path.exists(new) is None:
        os.mkdir(new)
    shutil.move(old,new)

def main():
    for a in os.listdir("./"):
        a_path=os.path.join(os.getcwd(),a)
        if os.path.isfile(a) is True:
            extension=a.split(".")[1].strip()
            new_path=os.path.join(path,extension)
            create_folder(new_path)
            move_file(a_path,new_path)
        else:
            pass

if __name__=="__main__":
    main()


