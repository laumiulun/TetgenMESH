import runtest

# IMPORT INPUT FILENAME
inname=runtest.inname
outname=inname[:-4]+'.1.vtk'

# READ INPUT FILE
with open(inname) as f:
    out=[]
    for line in f:
        line = line.split()
        if line:
            line=[str(i) for i in line]  # convert to str
            out.append(line)

# COUNTS THE NUMBER OF ROWS AND COLUMNS
NumsRows=len(out)
NumsColu=(len(out[0]))

# NUMBER OF ATTRIBUTES
NumsA=NumsColu-3

# FORMAT ATTRIBUTES 
x=[]
for i in range(NumsRows):
    x.append([])
    for j in range(NumsA):
        x[i].append(0)
        x[i][j]=out[i][j+3]

# OUTPUT INTO VTK
with open (outname, "a+") as f:
    f.write('\n')
    M= 'POINT_DATA ' + str(NumsRows)+ '\n'
    f.write(M)
    for j in range(NumsA):
        M='SCALARS Scalars_'+str(j+1)+' float \nLOOKUP_TABLE default \n'
        f.write(M)
        for i in range(NumsRows):
            f.write(x[i][j])
            f.write('\n')


   


