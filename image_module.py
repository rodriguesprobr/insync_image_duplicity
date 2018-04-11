#!/usr/bin/python
# -*- coding: utf8 -*-

###
#title           :image_module.py
#description     :Image duplicate module with the methods.
#author          :Fernando de Assis Rodrigues
#date            :20170411
#usage           :import image_module
#notes           :https://github.com/rodriguesprobr/insync_image_duplicity
#python_version  :3.7
###

import os, filecmp
def list(type, path):
	list = os.scandir(path)
	files = []
	for entry in list:
		if entry.is_dir():
			list_duplicities(str(path+"/"+entry.name))
		if entry.is_file():
			files.append(entry)
	files = sorted(files, key=lambda e: e.name, reverse=True)
	#files = sorted(files, reverse=True)
	#compararfiles(files, path)
	#print(files)
	if type == "stdout":
		for i in files:
			print(i.name)
	elif type == "return": 
		return files

def rm(type, path):
	files = list("return", path)
	for file_a in files:
		for file_b in files:
			if file_a != file_b:
				if filecmp.cmp(str(path + "/" + file_a.name), str(path + "/" + file_b.name)):
					if type == "stdout":
						print("rm " + path + "/" + file_b.name)
					files.remove(file_b)
