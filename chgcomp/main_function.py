# coding: utf-8
#  Copyright (c) 2020 Kumagai group.
import tarfile

import numpy as np

from pymatgen.io.vasp import Chgcar


def compress_isosurface(args):
    c: Chgcar = args.chgcar
    raw_data = c.data["total"]
    ngx, ngy, ngz = [bin(g)[2:].zfill(10) for g in c.dim]
    c_max = c.data['total'].max()
    mask = raw_data > float(args.level * c_max)
    bit_array = mask.astype(int).T.flatten()

    s = c.structure
    result = s.to("POSCAR") + f"{int(ngx, 2)} {int(ngy, 2)} {int(ngz, 2)} \n"

    for bit in bit_array:
        result += str(bit)
        result += " "
    suffix = args.suffix
    if suffix is None:
        suffix = int(float(args.level) * 1000)
    _write_file(result, f"CHGCAR_{suffix}")

    with tarfile.open(f"chgcar_{suffix}.tar.gz", mode='w:gz') as tar:
        tar.add(f"CHGCAR_{suffix}")


def compress_isosurfaces(args):
    c: Chgcar = args.chgcar
    raw_data = c.data["total"]
    c_max = c.data['total'].max()
    levels = np.linspace(0, 1, 8, endpoint=False)[1:]
    x_array = np.array([0]*c.ngridpts)
    for level in levels:
        mask = raw_data > float(level * c_max)
        x_array += mask.astype(int).T.flatten()

    s = c.structure
    header = s.to("POSCAR") + f"{c.dim[0]} {c.dim[1]} {c.dim[2]}" + "\n"

    for n, level in enumerate(levels):
        result = ""
        for x in x_array:
            result += str(int(int(x) >= n+1))
            result += " "
        a_file = header + result
        _write_file(a_file, f"CHGCAR_{int(level*1000)}")
        with tarfile.open(f"chgcar_{int(level*1000)}.tar.gz", mode='w:gz') as tar:
            tar.add(f"CHGCAR_{int(level*1000)}")


def _write_file(content, filename: str):
    with open(filename, 'w') as f:
        f.write(content)
