# InSync 1.x Image Duplicity
A Python 3.x script to deal with duplicity issues found on Insync 1.x versions, running on GNU/Linux distros.

To run you need Python 3.x installed with os and filecmp modules available.

First you need to config the directory path where Google Photos are stored in your computer. Just update the path variable on run.py

Then, it's just type python3 run.py > output.text and the script will generate a list with the rm commands that need to be run, manually (and safely).
 
