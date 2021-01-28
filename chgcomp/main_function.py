# coding: utf-8
#  Copyright (c) 2020 Kumagai group.

import pickle
import numpy as np

from pymatgen.io.vasp import Chgcar


def compress_isosurface(args):
    c: Chgcar = args.chgcar
    raw_data = c.data["total"]
    ngx, ngy, ngz = [bin(g)[2:].zfill(10) for g in c.dim]
    c_max = c.data['total'].max()
    mask = raw_data > float(args.level * c_max)
    bit_array = mask.astype(int).T.flatten()
    stream = "".join(bit_array.astype(str)) + ngx + ngy + ngz
    bin_stream = int(stream, 2)

    with open(f'isosurface_{args.level}.pickle', 'wb') as f:
        pickle.dump((c.structure, bin_stream), f, protocol=4)


def decompress_isosurface(args):
    with open(f'{args.isurf}', 'rb') as f:
        s, b = pickle.load(f)

    bin_stream = bin(b)
    stream, ngx, ngy, ngz = bin_stream[2:-30], bin_stream[-30:-20], bin_stream[-20:-10], bin_stream[-10:]
    ngrid = int(ngx, 2)*int(ngy, 2)*int(ngz, 2)
    true_stream = stream.zfill(ngrid)
    result = s.to("POSCAR") + f"{int(ngx, 2)} {int(ngy, 2)} {int(ngz, 2)} \n"
    for bit in true_stream:
        result += bit
        result += " "
    suffix = args.suffix
    if suffix is None:
        suffix = int(float(args.isurf[11:-7]) * 1000)
    _write_file(result, f"CHGCAR_{suffix}")


def compress_isosurfaces(args):
    c: Chgcar = args.chgcar
    raw_data = c.data["total"]
    c_max = c.data['total'].max()
    levels = np.linspace(0, 1, 8, endpoint=False)[1:]
    x_array = np.array([0]*c.ngridpts)
    for level in levels:
        mask = raw_data > float(level * c_max)
        x_array += mask.astype(int).T.flatten()

    x_stream = "".join(x_array.astype(str))
    bin_stream = int(x_stream, 8)

    with open(f'isosurface_slices.pickle', 'wb') as f:
        pickle.dump((c.structure, c.dim, bin_stream),
                    f, protocol=4)


def decompress_isosurfaces(args):
    with open(f'{args.isurf}', 'rb') as f:
        s, dim, x = pickle.load(f)

    header = s.to("POSCAR") + f"{dim[0]} {dim[1]} {dim[2]}" + "\n"
    x_stream = oct(x)[2:]
    true_x_stream = x_stream.zfill(dim[0]*dim[1]*dim[2])

    levels = np.linspace(0, 1, 8, endpoint=False)[1:]
    for n, level in enumerate(levels):
        result = ""
        for x in true_x_stream:
            result += str(int(int(x) >= n+1))
            result += " "
        a_file = header + result
        _write_file(a_file, f"CHGCAR_{int(level*1000)}")


def _write_file(content, filename: str):
    with open(filename, 'w') as f:
        f.write(content)
