# InSync 1.x Image Duplicity
A Python 3.x script to deal with duplicity issues found on Insync 1.x versions, running on GNU/Linux distros.

To run you need Python 3.x installed with os and filecmp modules available.

First, you need to config the directory path where Google Photos are stored on your computer. Just update the path variable on run.py

Then, it's type `python3 run.py > output.sh` on a Terminal  and the script will generate a list of the rm commands. Right now, the output file need to be run manually (and safely).
 
