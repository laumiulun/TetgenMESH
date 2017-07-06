#TetgenMESH

## Overview ##

Tetgen is a program developed by Weierstrass Institute of Applied Analysis and Stochastics (WISA) to generate tetrahedral meshes of any 3D polyhedral domains. 

TetgenMESH is developed as a script to provide FALCON(SubPackage of MOOSEFrameWork) with the necessary input mesh data.

This tutorial will be separate into two parts.

**Part 1** will be covering the running of Tetgen Meshing scripts

**Part 2** will be covering the conversion from VTK Mesh to Exodus Mesh

## Requirements ##
* Python 2.7 or 3.6.1 
* C++ compiler 
* Tetgen 1.5
* Cubit

## Compile and Install Tetgen ##
In-order to use TetGen, first download TetGen v1.5 from 

[Tetgen1.5](http://wias-berlin.de/software/tetgen/)

Before compiling tetgen, first put all sources files, **tetgen.h**, **tetgen.cxx**, and **predicates.cxx** and **makefile** into one directory. 

You also need to specify the C++ compiler to be used( Default is GNU C++ compiler)

To compile Tetgen, first navigate to the directory TetGen is located, which we will compile predicates.cxx first to get an object file:
	
	g++ -c predicates.cxx

To compile TetGen into a executable file, use the following command:
	
	g++ -o tetgen tetgen.cxx predicates.o -lm

Tetgen is provided if you clone falcon directly from github, but requires indivduial user to compile it. Tetgen is located in **falcon/tpl/tetgen**. To compile tetgen, simply navigate to the folder and follow the instruction above. 

## Input File ##
TetgenMESH is design to accept two different formats: **ROCKWORKS** and **PETREL**

### ROCKWORKS ###
The input file will consist of XYZ and one set of attribute(if any). The number of attributes will be the number of files inside the test folder. 

A two files attribute example will be:

`example.<attribute1>.txt`

`example.<attribute2>.txt`
 
And each file will have the format of with space delimited 

> 	X  Y  Z Attributes 1 



TetgenMESH will compare the XYZ coordinates of each files

### PETREL ###
The input file is will be consist of XYZ and any numbers of attributes. The format of the input file is as follow:

The end of the header must include `END` to signify the scripts as the end of the header

>| X | Y | Z | Attributes 1 | Attributes 2 | Attributes n |

An example input file has been provided:
[Example Input File](https://raw.githubusercontent.com/laumiulun/TetgenMESH/master/Gamma.txt)

## Using TetgenMESH ##

To run the scripts, simply navigate to the folder your test is located and enter the following command:

    $../scripts/tetgenMESH.sh

The scripts will then ask for input format and input name

The output file will be a in an .VTK format which can be open with many open source applications(PARAVIEW)

## VTK Mesh to Exodous Mesh Conversion ##

To convert VTK Mesh into Exodous:

1. Load the VTK mesh **example.vtk** into ParaView, and "save data" in  Exodus format as **example.e**.
2. Load the **example.e** back into ParaView and "save data" in **example.csv** as CSV format with the reordered nodal attributes
3. Remove all the double commas on the first line in "example.csv"

	If you are using vi as the editor, type the follow to remove the commas:
	
		1%s/,/ /g
	This replaces all commas from the 1st line and replace it with space. 

4. 
5. 


## Contact ##
This 

 Developer: Miu Lun Lau
