import os
import sys
import subprocess

def findlocation(keyword):
    string = str(keyword)
    for s in list:
        if string in str(s):
            out=list.index(s)
    return out

inname=input('Enter Input File Name: ')
outname=inname[:-3]+'node'

# OPEN INPUT FILE(TXT)
with open(inname) as f:
    out=[]
    for line in f:
        line = line.split()
        if line:
            line=[str(i) for i in line]  # convert to str
            out.append(line)
list = out

locat=int(findlocation('END'))

del out[0:locat+1]           
# NUMBER OF ROWS AND COLUMNS
NumsRows=len(out)
NumsColu=(len(out[0]))

NullV=int(-10000)

# ORGANIZE DATA
x=[]
for j in range(NumsRows):
    x.append([])
    for i in range(NumsColu):
        x[j].append(0)
        if float(out[j][i])<NullV:
            x[j][i]=0
        else:
            x[j][i]=out[j][i]
        
# ADD NUMBERING TO THE FRONT OF EACH NODES
for i in range(NumsRows):
    x[i].insert(0,i+1)

    
# OUTPUT FILES WITH ADDED HEADER FOR INPUT TO TETGEN
with open(outname, "w+") as f:
    M=(str(NumsRows)+' 3 1 0''\n')
    f.write(M)
    for j in range(len(x)):
        for i in range(len(x[0])):
                L=(str(x[j][i])+' ')
                f.write(L)
        f.write('\n')

# STAT OUTPUT
print('OK')
print('Nodes:',NumsRows)
"""-------------------------------------------------------------------------------------------------------------"""

# CALL PROCESS TO RUN TETGEN
os2=os.getcwd()
os3=os.path.join(os2,outname)

output=("tetgen -kNEF "+outname)

subprocess.call(output,shell=True)
