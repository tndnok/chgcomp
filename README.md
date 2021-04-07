Tutorial
---------------------------------------------------------
## 1. Requirements
  - Python 3.7 or higher
  - pymatgen
  
## 2. Compress CHGCAR to single isosurface
- prepare CHGCAR file
```
% ls
CHGCAR
```
- show help
```
% alias chgcomp="python PATH_TO_CHGCOMP/chgcomp/chgcomp/main.py"
% chgcomp -h 
usage: main.py [-h]
               {compress_isosurface,ci,compress_isosurfaces,cis}
               ...

positional arguments:
  {compress_isosurface,ci,compress_isosurfaces,cis}

optional arguments:
  -h, --help            show this help message and exit
```
- use ci command (e.g., set isosurface level to 20% of max value) 
```
% ls  
CHGCAR 
% chgcomp ci -c CHGCAR -l 0.2  
% ls  # compressed files are written in CHGCAR_200 and chgcar_200.tar.gz (200 comes from 0.2 * 1000)
CHGCAR  CHGCAR_200  chgcar_200.tar.gz
```
- Examples of compressed file sizes (52M -> 5.7M -> 28K)
```
% du -sh *
 52M	CHGCAR
5.7M	CHGCAR_200
 28K	chgcar_200.tar.gz
```

## 2. Compress CHGCAR to 7 sliced isosurfaces
```
% chgcomp cis -c CHGCAR 
% ls  
CHGCAR            CHGCAR_375        CHGCAR_750        chgcar_200.tar.gz chgcar_500.tar.gz chgcar_875.tar.gz
CHGCAR_125        CHGCAR_500        CHGCAR_875        chgcar_250.tar.gz chgcar_625.tar.gz
CHGCAR_250        CHGCAR_625        chgcar_125.tar.gz chgcar_375.tar.gz chgcar_750.tar.gz
% du -sh *
 52M	CHGCAR
5.7M	CHGCAR_125
5.7M	CHGCAR_250
5.7M	CHGCAR_375
5.7M	CHGCAR_500
5.7M	CHGCAR_625
5.7M	CHGCAR_750
5.7M	CHGCAR_875
 36K	chgcar_125.tar.gz
 28K	chgcar_200.tar.gz
 28K	chgcar_250.tar.gz
 20K	chgcar_375.tar.gz
 16K	chgcar_500.tar.gz
 16K	chgcar_625.tar.gz
 12K	chgcar_750.tar.gz
 12K	chgcar_875.tar.gz
```

