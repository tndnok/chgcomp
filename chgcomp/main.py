# coding: utf-8
#  Copyright (c) 2020 Kumagai group.

import argparse
import sys

from pymatgen import Structure
from pymatgen.io.vasp import Chgcar

from chgcomp.main_function import freeze_isosurface, unpack_isosurface


def parse_args(args):

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers()

    # -- freeze_isosurface -------------------------------
    parser_freeze_isosurface = subparsers.add_parser(
        name="freeze_isosurface",
        description="",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        aliases=['fi'])

    parser_freeze_isosurface.add_argument("-c", "--chgcar", required=True,
                                          type=Chgcar.from_file)
    parser_freeze_isosurface.add_argument("-l", "--level", default=0.5,
                                          type=float)
    parser_freeze_isosurface.set_defaults(func=freeze_isosurface)

    # -- unpack_isosurface -------------------------------
    parser_unpack_isosurface = subparsers.add_parser(
        name="unpack_isosurface",
        description="",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        aliases=['ui'])

    parser_unpack_isosurface.add_argument("-p", "--poscar", required=True,
                                          type=Structure.from_file)
    parser_unpack_isosurface.add_argument("-i", "--isurf", required=True,
                                          type=str)
    parser_unpack_isosurface.set_defaults(func=unpack_isosurface)

    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])
    args.func(args)


if __name__ == "__main__":
    main()


