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
    
# FUNCTION TO OUTPUT ERROR
def fileERROR(command,message):
    try:
        f= open(command)
    except FileNotFoundError:
        print(bcolors.RED+'ERROR: ' +str(message) +' NOT FOUND'+bcolors.N)
        sys.exit()
        
# FUNCTION REDUNDANCY
def redundancy(filetocheck):
    for i in range(len(filetocheck)-1):
        
        #OPEN first file:
        with open(filetocheck[i]) as f:
            out=[]
            for line in f:
                line = line.split()
                if line:
                    line=[str(i) for i in line]  # convert to str
                    out.append(line)
        del out[0]
        
        #OPEN second file:
        with open(filetocheck[i+1]) as f:
            out2=[]
            for line in f:
                line = line.split()
                if line:
                    line=[str(i) for i in line]  # convert to str
                    out2.append(line)
        del out2[0]                   

        # Compare the 2 files
        for i in range(len(out)):
            for j in range(3):
                if out[i][j] == out2[i][j]:
                    continue
                else:
                    print('ERROR, XYZ DOES NOT MATCH')
                    print(os.path.basename(filetocheck[i+1]),' COORDINATES DOES NOT MATCH')
                    sys.exit()
    print('REDUNDANCY CHECK OK')

def readfile(filenameinput):
    with open(filenameinput) as f:
        out=[]
        for line in f:
            line = line.split()
            if line:
                line=[str(i) for i in line]  # convert to str
                out.append(line)
    return out

# START OF THE SCRIPTS
#############################################################################

print("-"*50)
# GET CURRENT WORKING DIRECTORY AND MOVE INTO TEST DIRECTORY
os2=os.getcwd()   # OS2: Current working directory

# ASK FOR USER INPUT TO THE FILE
usrname=input(bcolors.BOLD+'Enter Input File Name: '+bcolors.N)
inname=os.path.join(os2,usrname)

print('usrname:',usrname)
print('inname:',inname)

# Find files
i=0
j=0
x=[]
for root, dirs, files in os.walk(os2, topdown=True):    # Find all files in the the dir
    for name in files:
        if usrname in name:
            j+=1
            x.append([])
            x[i-1]=(os.path.join(root, name))

#print(bcolors.BOLD+'Input WD:'+ bcolors.N + inname)

f=inname.find(".")
outname=inname[0:f]+'.node'  # print .node absolute filepath

#print(bcolors.BOLD+'Output WD:'+bcolors.N + outname)

#FILE NOT FIND ERROR
fileERROR(inname,"INPUT FILE")

# OPEN INPUT FILE(TXT)
##with open(inname) as f:
##    out=[]
##    for line in f:
##        line = line.split()
##        if line:
##            line=[str(i) for i in line]  # convert to str
##            out.append(line)

out=readfile(inname)



"""-------------------------------------------------------------------------------------------------------------"""
# FILE FORMAT CHECK
# ASK FOR USER INPUT FORMAT
formatname=input(bcolors.BOLD+"ENTER FORMATS(ROCKWORKS OR PETREL): " + bcolors.N)

if formatname == "ROCKWORKS":
    del out[0]

    n=usrname.find('.')
    string=usrname[:n]  # remove .txt and attribute subset
    fileformat='.txt'
    # Find files
    i=0
    j=0
    x=[]
    for root, dirs, files in os.walk(os2, topdown=True):    # Find all files in the the dir
        for name in files:
            if string in name and fileformat in name:
                j+=1
                x.append([])
                x[i-1]=(os.path.join(root,name))
            
    # Call redundancy FUNCTION
    redundancy(x)

    # Extract XYZ data
    with open(x[0]) as f:
            out=[]
            for line in f:
                line = line.split()
                if line:
                    line=[str(i) for i in line]  # convert to str
                    out.append(line)
            del out[0]
    xyz=[]
    for i in range(len(out)):
        xyz.append([])
        for j in range(3):
            xyz[i].append(0)
            xyz[i][j]=float(out[i][j])


    # Combine into one VTK
    att=[]
    for i in range(len(x)):

        # OPEN AND READ FILES
        with open(x[i]) as f:
            out=[]
            for line in f:
                line = line.split()
                if line:
                    line=[str(i) for i in line]  # convert to str
                    out.append(line)
            del out[0]

        # EXTRACT ATT VALUES
        att.append([])
        for k in range(len(out)):
            att[i].append(0)
            att[i][k]=float(out[k][3])

    # Transpose the att
    tatt=[list(x) for x in zip(*att)]

    # Combine xyz and attributes
    sourceout=[]
    for i in range(len(xyz)):
        sourceout.append([])
        sourceout[i]=xyz[i]+tatt[i]

    with open (outname,"w+") as f:
        
        for i in range(len(sourceout)):
            for j in range(len(sourceout[0])):
                f.write(str(sourceout[i][j]))
                f.write(' ')
            f.write('\n')

    inname=outname
elif formatname == "PETREL":
    list = out
    locat=int(findlocation('END'))
    del out[0:locat+1]
    
else:
    print(bcolors.RED +"ERROR: FILE FORMAT NOT FOUND" + bcolors.N)
    exit()

"""-------------------------------------------------------------------------------------------------------------"""

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

#FIND TETGEN DIR
os5=os.path.dirname(os.path.dirname(os2))
tetgen='tetgen.exe'
for root, dirs, files in os.walk(os5, topdown=True):    # Find all files in the the dir
    for name in files:
        if tetgen in name:
            pathtotetgen=(os.path.join(root, name))

# 
output=(pathtotetgen + " -kNEF " + outname)


subprocess.call(output,shell=True)
print(bcolors.GREEN+'Tetgen OK'+bcolors.N)

"""-------------------------------------------------------------------------------------------------------------"""

outname2=outname[:-4]+'1.vtk'

if formatname == 'PETREL':
    NullV=int(-998)
elif formatname == 'ROCKWORKS':
    NullV=int(-10000)

# NUMBER OF ATTRIBUTES (subtracting XYZ)
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
