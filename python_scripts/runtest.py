#Include Subprocess
import os
import sys
import subprocess

# FUNCTION to FIND LOCATION
def findlocation(keyword):
    string = str(keyword)
    for s in list:
        if string in str(s):
            out=list.index(s)
    return out

# Class of Colors
class bcolors:
    N='\033[0m'             #Normal
    BOLD = '\033[1m'        #Bold
    UNDERL = '\033[4m'      #Underline
    RED = '\033[91m'        #RED
    GREEN = '\033[42m'      #GREEN
    
# Function to output error
def fileERROR(command,message):
    try:
        f= open(command)
    except FileNotFoundError:
        print(bcolors.RED+'ERROR: ' +str(message) +' Not Found'+bcolors.N)
        exit()

# GET CURRENT WORKING DIRECTORY AND MOVE INTO TEST DIRECTORY
os2=os.getcwd()   # OS2: Current working directory

# ASK FOR USER INPUT TO THE FILE
usrname=input(bcolors.BOLD+'Enter Input File Name: '+bcolors.N)
inname=os.path.join(os2,usrname)
#print(bcolors.BOLD+'Input WD:'+ bcolors.N + inname)

f=inname.find(".")
outname=inname[0:f]+'.node'

#print(bcolors.BOLD+'Output WD:'+bcolors.N + outname)

# FILE NOT FIND ERROR
fileERROR(inname,"INPUT FILE")

# OPEN INPUT FILE(TXT)
with open(inname) as f:
    out=[]
    for line in f:
        line = line.split()
        if line:
            line=[str(i) for i in line]  # convert to str
            out.append(line)
#del out[0]
list = out
locat=int(findlocation('END'))

del out[0:locat+1]

# NUMBER OF ROWS AND COLUMNS
NumsRows=len(out)
NumsColu=(len(out[0]))
print('Reading Input File'+"."*15,end="")

# ORGANIZE DATA INTO COLUMNS AND ROWS
x=[]
for j in range(NumsRows):
    x.append([])
    for i in range(NumsColu):
        x[j].append(0)
        x[j][i]=out[j][i]

print(bcolors.BOLD+"[DONE]"+bcolors.N) 

# ADD NUMBERING TO THE FRONT OF EACH NODES
for i in range(NumsRows):
    x[i].insert(0,i+1)
    
# OUTPUT FILES WITH ADDED HEADER FOR INPUT TO TETGEN
print('Convert to .node'+"."*17,end="")

with open(outname, "w+") as f:
    M=(str(NumsRows)+' 3 1 1''\n')
    f.write(M)
    for j in range(len(x)):
        for i in range(len(x[0])):
                L=(str(x[j][i])+' ')
                f.write(L)
        f.write('\n')

# STATE OUTPUT
print(bcolors.BOLD+"[DONE]"+bcolors.N) 
print('Number of Nodes:',NumsRows)
"""-------------------------------------------------------------------------------------------------------------"""

### CALL PROCESS TO RUN TETGEN
print(bcolors.BOLD+"CALLING TETGEN..."+bcolors.N)
print("-"*50)

os3m=os.path.basename(os2)
os3=os2[:-len(os3m)]


pathtotetgen=os.path.join(os3,'TetgenMesh/tpl/tetgen/tetgen')
output=(pathtotetgen + " -kNEF " + outname)

subprocess.call(output,shell=True)

print(bcolors.GREEN+'Tetgen OK'+bcolors.N)

"""-------------------------------------------------------------------------------------------------------------"""

outname2=outname[:-4]+'1.vtk'

# READ INPUT FILE
with open(inname) as f:
    out=[]
    for line in f:
        line = line.split()
        if line:
            line=[str(i) for i in line]  # convert to str
            out.append(line)
            
del out[0:locat+1]
# COUNTS THE NUMBER OF ROWS AND COLUMNS
NumsRows=len(out)
NumsColu=(len(out[0]))

NullV=int(-998)
# NUMBER OF ATTRIBUTES
NumsA=NumsColu-3

# FORMAT ATTRIBUTES 
x=[]
for i in range(NumsRows):
    x.append([])
    for j in range(NumsA):
        x[i].append(0)
        if float(out[i][j])<NullV:        
            x[i][j]=-1;
        else:
            x[i][j]=out[i][j+3]

print("-"*50)
print("Writing Attributes...")

# OUTPUT INTO VTK
with open (outname2, "a+") as f:
    f.write('\n')
    M= 'POINT_DATA ' + str(NumsRows)+ '\n'
    f.write(M)
    for j in range(NumsA):
        M='SCALARS Scalars_'+str(j+1)+' float \nLOOKUP_TABLE default \n'
        f.write(M)
        for i in range(NumsRows):
            if float(x[i][j])<NullV:
                f.write('-1.0');
                f.write('\n')
            else:
                f.write(x[i][j])
                f.write('\n')
        print("Writing Attributes ["+str(j+1)+']')
    print(bcolors.BOLD+"[DONE]"+bcolors.N)

print("-"*50)
print(bcolors.GREEN+bcolors.BOLD+"Finish"+bcolors.N)



