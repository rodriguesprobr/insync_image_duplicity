#!/usr/bin/python
# -*- coding: utf8 -*-

path = "/home/orionx/Downloads/11" # Insert your Google Photo folder, with full path. Example: /home/user/your@email/Google Photos

import importlib, imageClass as ic

# List command that retrieves the files that will be analyzed. Made for debugging purposes and it's not required to be enabled.
# ic.list("stdout", path)

# Enable the command below to run the safe option.
# The rm command will make a stdout string, with a bunch of rm commands to remove all duplicates, manually.
# To run, I suggest something like python3 run.py >> to a output.text, with this command enabled.
ic.rm("stdout", path)
