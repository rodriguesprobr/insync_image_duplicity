#!/usr/bin/python
# -*- coding: utf8 -*-

###
#title           :image_module.py
#description     :Image duplicate module.
#author          :Fernando de Assis Rodrigues
#date            :20180503
#usage           :import image_module
#notes           :https://github.com/rodriguesprobr/insync_image_duplicity
#python_version  :3.5.2
###

import os, filecmp, image_module as im

def find_duplicates(path):
    list = os.scandir(path)
    files = []
    dirs = []
    for entry in list:
        if entry.is_dir():
            dirs.append(entry)
        elif entry.is_file():
            files.append(entry)
    compare(files, path)
    for d in dirs:
        find_duplicates(path + "/" + d.name)

def compare(files, path):
    for file_a in files:
        for file_b in files:
            if file_a != file_b:
                if filecmp.cmp(str(path + "/" + file_a.name), str(path + "/" + file_b.name)):
                    print("rm -f  " + \
                        path.replace("'", "\'").replace(" ", "\ ").replace("(", "\(").replace(")", "\)") + \
                        "/" + \
                        file_b.replace("'", "\'").name.replace(" ", "\ ").replace("(", "\(").replace(")", "\)"))
                    files.remove(file_b)
