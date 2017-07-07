# TetgenMESH

## Overview ##

Tetgen is a program developed by Weierstrass Institute of Applied Analysis and Stochastics (WISA) to generate tetrahedral meshes of any 3D polyhedral domains. 

TetgenMESH is script developed to provide [FALCON](https://github.com/idaholab/falcon)(Application of [MooseFramework](http://mooseframework.org/)) with the necessary input mesh data.

This tutorial will be separate into two parts.

**Part 1** will be covering the running of Tetgen Meshing scripts

**Part 2** will be covering the conversion from VTK Mesh to Exodus Mesh

## Requirements ##
* [Python 2.7.2 or 3.6.1](https://www.python.org/downloads/) 
* C++ compiler
* [Tetgen1.5](http://wias-berlin.de/software/tetgen/)
* [Cubit 5.2](https://cubit.sandia.gov)

## Compile and Install Tetgen ##
In-order to use TetGen, first download TetGen v1.5 from [Tetgen1.5](http://wias-berlin.de/software/tetgen/)

Before compiling tetgen, first put all sources files, **tetgen.h**, **tetgen.cxx**, and **predicates.cxx** and **makefile** into one directory. 

You also need to specify the C++ compiler to be used(Default is GNU C++ compiler)

To compile Tetgen, first navigate to the directory Tetgen is located, and compile **predicates.cxx** to get an object file:
	
	
`g++ -c predicates.cxx`

To compile TetGen into a executable file, use the following command:
	
`g++ -o tetgen tetgen.cxx predicates.o -lm`

Tetgen is included if you clone falcon directly from github, but requires indivduial user to compile it. Tetgen is located in **falcon/tpl/tetgen**. To compile tetgen, navigate to the folder contain Falcon and follow the instruction above. 

## Input Files ##
TetgenMESH is design to accept two different formats: **ROCKWORKS** and **PETREL**

### ROCKWORKS ###
The input file will contain nodal coordinates(XYZ) and one set of attribute(if any). The number of attributes will be the number of files inside the test folder. 

A two files attribute example will be:

`example.<Attribute1>.txt`

`example.<Attribute2>.txt`
 
And each file will have the nodal coordinates and corresponding attribute data with the format: 

		< X > < Y > < Z > < Attributes 1 >

TetgenMESH will check and compare the nodal coordinates of each files

An example input file has been provided:
[Rockworks Input File](https://github.com/laumiulun/TetgenMESH/blob/master/tests/rockworks/example.porosity.txt)

### PETREL ###
The input file is will be consist of nodal coordinates and any numbers of attributes. The format of the input file is as follow:

The end of the header must include `END` to signify the scripts as the end of the header
#### Header ####

		< X > < Y > < Z > < Attributes 1 > < Attributes 2 > < Attributes n >

An example input file has been provided:
[Petrel Input File](https://github.com/laumiulun/TetgenMESH/blob/master/tests/petrel/example.txt)


## Using TetgenMESH ##

To run the scripts, simply navigate to the folder your test is located and enter the following command:

##### Python 3.7 :

`$../scripts/tetgenMESH.sh`

##### Python 2.7 :
	
`$../scripts2.7/tetgenMESH2.7.sh`

The scripts will then ask for input format and input name

The output file will be a in .VTK format which can be open with many open source post-processing software packages, for example, [ParaView](https://www.paraview.org/).

## VTK Mesh to Exodous Mesh Conversion ##

To convert VTK Mesh into Exodous:

1. Load the VTK mesh **example.vtk** into ParaView, and "save data" in  Exodus format as **example.e**.
2. Load the **example.e** back into ParaView and "save data" in **example.csv** as CSV format with the reordered nodal attributes
3. Remove all the double commas on the first line in **"example.csv"**, and save. 

	If you are using vi as editor, type the following:
	
		1%s/,/ /g
	This replaces all commas from the 1st line and replace it with space. 

4. **example.e** does not contain Sideset info. Load **"example.e"** in Cubit and assign Sideset IDs to the boundaries. Set the element of type from **"TERA"** to **"TERA4"**, and overwrite **"example.e"**

There should be two files if you follow all the step above:

1. **"example.e"** contains a pure Exodus mesh file with Subset IDs
2. **"example.csv"** a CSV file containing nodal attributes 


## Contact ##

*	[Github address](https://github.com/laumiulun/TetgenMESH)
*	Developer: Miu Lun Lau
* 	Email: miulun.lau@inl.gov
