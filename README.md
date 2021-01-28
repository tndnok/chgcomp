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
               {compress_isosurface,ci,decompress_isosurface,di,compress_isosurfaces,cis,decompress_isosurfaces,dis}
               ...

positional arguments:
  {compress_isosurface,ci,decompress_isosurface,di,compress_isosurfaces,cis,decompress_isosurfaces,dis}

optional arguments:
  -h, --help            show this help message and exit
```
- use ci command (e.g., set isosurface level to 30% of max value) 
```
% chgcomp ci -c CHGCAR -l 0.3  
% ls  # pickle file is dumped
CHGCAR  isosurface_0.3.pickle
```
- pickle file size is 1/200 of original CHGCAR file
```
% du -sh *
8.9M	CHGCAR
48K	isosurface_0.3.pickle
```

## 3. Decompress single isosurface
- use di command 
```
% ls
isosurface_0.3.pickle 
% chgcomp di -i isosurface_0.3.pickle 
% ls 
CHGCAR_300               isosurface_0.3.pickle
```
- open with VESTA
```
% open -a VESTA CHGCAR_300
```

## 4. Compress/Decompress CHGCAR to 7 sliced isosurfaces
```
% chgcomp cis -c CHGCAR 
% ls  # pickle file is dumped
CHGCAR  isosurface_slices.pickle  POSCAR
% du -sh *
8.9M	CHGCAR
4.0K	POSCAR
152K	isosurface_slices.pickle
% chgcomp dis -i isosurface_slices.pickle
% ls
CHGCAR                   CHGCAR_250               CHGCAR_500               CHGCAR_750               isosurface_slices.pickle
CHGCAR_125               CHGCAR_375               CHGCAR_625               CHGCAR_875
% open -a VESTA CHGCAR_*
```

