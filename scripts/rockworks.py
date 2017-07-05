import os
import sys

import runtest

Cur_dir=os.getcwd()
filein=runtest.inname

# Function redundancy 
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

# change input name
n=filein.find('.')
string=filein[:n]  # remove .txt from end
fileformat='.txt'

# Find files
i=0
j=0
x=[]
for root, dirs, files in os.walk(Cur_dir, topdown=True):    # Find all files in the the dir
    for name in files:
        if string in name and fileformat in name:
            j+=1
            x.append([])
            x[i-1]=(os.path.join(root, name))
            

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

# Combine into a txt file for tetgen
##q=os.path.basename(x[0]).find('<')
##s=os.path.basename(x[0])
##rock_name=s[:q]+'txt'

with open ('out.txt',"w+") as f:
    f.write('ROCKWORKS DATA \n')
    for i in range(len(sourceout)):
        for j in range(len(sourceout[0])):
            f.write(str(sourceout[i][j]))
            f.write(' ')
        f.write('\n')
        




        
