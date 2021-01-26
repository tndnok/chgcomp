Installation instructions
---------------------------------------------------------
## 1. Requirements
  - Python 3.7 or higher
  - pymatgen
  
## 2. Compress CHGCAR-like file
- prepare CHGCAR file
```
% ls
POSCAR CHGCAR
% cat POSCAR
Mg1 O1
1.0
0.0000000000 2.1046630000 2.1046630000
2.1046630000 0.0000000000 2.1046630000
2.1046630000 2.1046630000 0.0000000000
Mg O
1 1
direct
0.0000000000 0.0000000000 0.0000000000 Mg
0.5000000000 0.5000000000 0.5000000000 O
```
- use fi command 
```
% alias chgcomp="python PATH_TO_CHGCOMP/chgcomp/chgcomp/main.py"
% chgcomp -h 
usage: main.py [-h] {freeze_isosurface,fi,unpack_isosurface,ui} ...

positional arguments:
  {freeze_isosurface,fi,unpack_isosurface,ui}

optional arguments:
  -h, --help            show this help message and exit
% chgcomp fi -h
usage: main.py freeze_isosurface [-h] -c CHGCAR [-i ILEVEL]

optional arguments:
  -h, --help            show this help message and exit
  -c CHGCAR, --chgcar CHGCAR
  -l LEVEL, --level LEVEL
```
- set isosurface level (e.g., 30% of max value)
```
% chgcomp fi -c CHGCAR -l 0.3  
% ls # pickle file is dumped
CHGCAR  isosurface_0.3.pickle  POSCAR
```
- pickle file size is 1/200 of original CHGCAR file
```
% du -sh *
8.9M	CHGCAR
4.0K	POSCAR
48K	isosurface_0.3.pickle
```

## 3. Decompress dumped file
- use POSCAR and *.pickle file
```
% ls
isosurface_0.3.pickle  POSCAR
```
- use ui command (do redirect output to file, e.g., CHGCAR_xx)
```
% chgcomp ui -h
usage: main.py unpack_isosurface [-h] -p POSCAR -i ILEVEL

optional arguments:
  -h, --help            show this help message and exit
  -p POSCAR, --poscar POSCAR
  -i ISURF, --isurf ISURF
% chgcomp ui -p POSCAR -i isosurface_0.3.pickle >| CHGCAR_30
```
- open with VESTA
```
% ls 
CHGCAR_30             POSCAR                isosurface_0.3.pickle
% open -a VESTA CHGCAR_30
```
