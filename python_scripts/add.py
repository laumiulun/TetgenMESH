import runtest

# IMPORT INPUT FILENAME
inname=runtest.inname
outname=inname[:-4]+'.1.vtk'

# READ INPUT FILE
##with open(inname) as f:
##    out=[]
##    for line in f:
##        line = line.split()
##        if line:
##            line=[str(i) for i in line]  # convert to str
##            out.append(line)
##del out[0]
out=runtest.out
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


print("Writing Attributes")

# OUTPUT INTO VTK
with open (outname, "a+") as f:
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


   


