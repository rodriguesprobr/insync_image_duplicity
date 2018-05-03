#!/usr/bin/python
# -*- coding: utf8 -*-

###
#title           :run.py
#description     :Run this script find duplicates images on Google Photos.
#author          :Fernando de Assis Rodrigues
#date            :20180503
#usage           :import image_module
#notes           :https://github.com/rodriguesprobr/insync_image_duplicity
#python_version  :3.5.2
###

import importlib, image_module as im

# Insert on the variable below your Google Photo full path. For example: /home/user/your@email/Google Photos
path = "/home/orionx/googledrive/Google Fotos"

im.find_duplicates(path)
