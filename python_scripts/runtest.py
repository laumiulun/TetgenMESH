import os
import sys
import subprocess
class bcolors:
    N='\033[0m'             #Normal
    BOLD = '\033[1m'        #Bold
    UNDERL = '\033[4m'      #Underline
    RED = '\033[91m'        #RED
    GREEN = '\033[42m'      #GREEN


inname=input('Enter Input File Name: ')
outname=inname[:-3]+'node'
#filename=input('Enter filename(with extension): ')
with open(inname) as f:
    out=[]
    for line in f:
        line = line.split()
        if line:
            line=[str(i) for i in line]  # convert to str
            out.append(line)

NumsRows=len(out)
NumsColu=(len(out[0]))

x=[]
for j in range(NumsRows):
    x.append([])
    for i in range(NumsColu):
        x[j].append(0)
        x[j][i]=out[j][i]

for i in range(NumsRows):
    x[i].insert(0,i+1)
# Output files to a txt to the corrospondig dir.
with open(outname, "w+") as f:
    M=(str(NumsRows)+' 3 1 1''\n')
    f.write(M)
    for j in range(len(x)):
        for i in range(len(x[0])):
                L=(str(x[j][i])+' ')
                f.write(L)
        f.write('\n')
print('OK')
print('Nodes:',NumsRows)
"""-------------------------------------------------------------------------------------------------------------"""
os2=os.getcwd()
os3=os.path.join(os2,outname)

output=("tetgen -kNEF "+outname)

subprocess.call(output,shell=True)
