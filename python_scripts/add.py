import runtest

inname=runtest.inname

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
    x[j]=out[j][3]


with open('Gamma.1.vtk', "a+") as f:
    M='POINT_DATA '+str(NumsRows)+ '\n'
    f.write(M)
    M='SCALARS cell_scalars float 1 \nLOOKUP_TABLE default \n'
    f.write(M)
    for i in range(NumsRows):
        f.write(x[i])
        f.write('\n')
    
   


