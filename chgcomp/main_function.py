# coding: utf-8
#  Copyright (c) 2020 Kumagai group.

import pickle
from pymatgen.io.vasp import Chgcar


def freeze_isosurface(args):
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


def unpack_isosurface(args):
    with open(f'{args.isurf}', 'rb') as f:
        s, b = pickle.load(f)

    print(s.to("POSCAR"))
    bin_stream = bin(b)
    stream, ngx, ngy, ngz = bin_stream[2:-30], bin_stream[-30:-20], bin_stream[-20:-10], bin_stream[-10:]
    print(int(ngx, 2), int(ngy, 2), int(ngz, 2))
    ngrid = int(ngx, 2)*int(ngy, 2)*int(ngz, 2)
    true_stream = stream.zfill(ngrid)
    result = ""
    for bit in true_stream:
        result += bit
        result += " "
    print(result)
