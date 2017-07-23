#==============================================================================
#
#  Program:   vtk2exodus
#
#==============================================================================

import os,sys

# FIND FILES
def find(name,path):
    for root, dirs, files in os.walk(path):
        files = [f for f in files if not f[0] == '.']   # Ignore hidden folder
        dirs[:] = [d for d in dirs if not d[0] == '.']  # Ignore hidden files
        if name in files:
            return os.path.join(root, name)

# FIND HOME DIRECTORY
from os.path import expanduser
os2=expanduser("~")

while True:
    print os.getcwd()
    filename=raw_input('Enter Absolute Path of the File: ')
    try:
        f=open(filename)
        break
    except BaseException:
        print '\n ERROR: INPUT FILE NOT FIND'
        
inname=filename
ename=inname[:-3]+"e"          # exodus name
csvname=inname[:-3]+".csv"      # CSV name
csvname2=inname[:-4]+".0.csv"   #CSV2name
# PARAVIEW PYTHON
#----------------------------------------------------#

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
examplevtk = LegacyVTKReader(FileNames=[inname])

# save data
SaveData(ename, proxy=examplevtk)

# create a new 'ExodusIIReader'
examplee = ExodusIIReader(FileName=[ename])
examplee.PointVariables = []

# save data
SaveData(csvname, proxy=examplee)

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...)

print("\n Done")
# MODIFY CSV FILE
#----------------------------------------------------#
with open(csvname2) as fin:
    lines = fin.readlines()
lines[0] = lines[0].replace(',','')

with open(csvname2, 'w') as fout:
    for line in lines:
        fout.write(line)
print("\n Commas Removed")

