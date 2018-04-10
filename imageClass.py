#!/usr/bin/python
# -*- coding: utf8 -*-
class Image:
	import os, filecmp
	def listarDiretorios(path):
		#print(path)
		list = os.scandir(path)
		listFiles = []
		for entry in list:
			if entry.is_dir():
				#print(path,"/",entry.name, sep="")
				listarDiretorios(str(path+"/"+entry.name))
			if entry.is_file():
				listFiles.append(entry.name)
		#listFiles = sorted(listFiles, key=lambda e: e.name, reverse=True)\
		listFiles = sorted(listFiles, reverse=True)
		compararArquivos(listFiles, path)
		#print(listFiles)
		#for i in listFiles:
		#	print(i)
		#if len(listFiles) == 0:
			#print(path," <-- VAZIO")

	def compararArquivos(listFiles, path):
		for arquivoA in listFiles:
			#print("ArquivoA "+arquivoA.name)
			for arquivoB in listFiles:
				print(arquivoA+" - "+arquivoB)
				if arquivoA != arquivoB:
					#print("ArquivoB "+arquivoB.name)
					if filecmp.cmp(str(path+"/"+arquivoA), str(path+"/"+arquivoB)):
						print("- é igual")
						listFiles.remove(arquivoB)

	def __init__(path):
		listarDiretorios("/home/orionx/googledrive/Google Fotos/2014/11")
