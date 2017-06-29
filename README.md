# TetgenMESH #

### Overview ###

Tetgen is a program developed by Weierstrass Institute of Applied Analysis and Stochastics (WISA) to generate tetrahedral meshes of any 3D polyhedral domains. TetgenMESH is developed as a submodule to provide FALCON(SubPackage of MOOSEFRAMEWORK) with the necessary input mesh data.

### Requirement ###
* Python 3.6.1 
* C++ compiler 
* Tetgen 1.5

### Compile and Install Tetgen ###
In-order to use TetGen, first download TetGen v1.5 from 

[Tetgen1.5](http://wias-berlin.de/software/tetgen/)

Before compiling tetgen, first put all sources files, **tetgen.h**, **tetgen.cxx**, and **predicates.cxx** and **makefile** into one directory. 

You also need to specify the C++ compiler to be used( Default is GNU C++ compiler)

To compile Tetgen, first navigate to the directory TetGen is located, which we will compile predicates.cxx first to get an object file:

	
	g++ -c predicates.cxx
	

To compile TetGen into a executable file, use the following command:
	
	g++ -o tetgen tetgen.cxx predicates.o -lm

Tetgen is provided if you clone falcon directly from github, but requires indivduial user to compile it. Tetgen is located in **falcon/tpl/tetgen**. To compile tetgen, simply navigate to the folder and follow the instruction above. 
 
### Environmental Variable ###
To use Tetgen executable outside of the file, navigate to the file using this command:

	vi ~/.bash_profile

Add the following line to the bottom as a path:
	
	export PATH="**ENTER YOUR OWN FILE PATH TO TETGEN EXE**:$PATH"

### Using TetGen Switch ###
TetGen has many synatax that governs its outputs, and the basic commands is:

    tetgen [SWITCH] [input_file]

All the switches for tetgen is below:

```
|Switch|Description|

|-p |Tetrahedralizes a piecewise linear complex (PLC).      |
|-Y |Preserves the input surface mesh (does not modify it). |
|-r |Reconstructs a previously generated mesh.              |
|-q |Refines mesh (to improve mesh quality).                |
|-R |Mesh coarsening (to reduce the mesh elements).         |
|-A |Assigns attributes to tetrahedra in different regions. |
|-a |Applies a maximum tetrahedron volume constraint.       |
|-m |Applies a mesh sizing function.                        |
|-i |Inserts a list of additional points.                   |
|-O |Specifies the level of mesh optimization.              |
|-S |Specifies maximum number of added points.              |
|-T |Sets a tolerance for coplanar test (default 10−8).     |
|-X |Suppresses use of exact arithmetic.                    |
|-M |No merge of coplanar facets or very close vertices.    |
|-w |Generates weighted Delaunay (regular) triangulation.   |
|-c |Retains the convex hull of the PLC.                    |
|-d |Detects self|-intersections of facets of the PLC.      |
|-z |Numbers all output items starting from zero.           |
|-f |Outputs all faces to .face file.                       |
|-e |Outputs all edges to .edge file.                       |
|-n |Outputs tetrahedra neighbors to .neigh file.           |
|-v |Outputs Voronoi diagram to files.                      |
|-g |Outputs mesh to .mesh file for viewing by Medit.       |
|-k |Outputs mesh to .vtk file for viewing by Paraview.     |
|-J |No jettison of unused vertices from output .node file. |
|-B |Suppresses output of boundary information.             |
|-N |Suppresses output of .node file.                       |
|-E |Suppresses output of .ele file.                        |
|-F |Suppresses output of .face and .edge file.             |
|-I |Suppresses mesh iteration numbers.                     |
|-C |Checks the consistency of the final mesh.              |
|-Q |Quiet: No terminal output except errors.               |
|-V |Verbose: Detailed information, more terminal output.   |
|-h |Help: A brief instruction for using TetGen.            |

```
### Input File

The input file is will be consist of XYZ and any number of attributes. The format of the input file is as follow:

| X | Y | Z | Attributes 1 | Attributes 2 | Attributes n |

An example input file has been provided:
[Example Input File](https://raw.githubusercontent.com/laumiulun/TetgenMESH/master/Gamma.txt)

In the inputfile, the 
### Using TetgenMESH

To run the scripts, simply navigate to the test folder and enter the following command:

    $../scripts/tetgenMESH.sh

The program will ask you to enter the name of the input file(txt).



### Contact ###
* Developer: Miu Lun Lau
