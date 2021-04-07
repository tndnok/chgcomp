# coding: utf-8
#  Copyright (c) 2020 Kumagai group.

import argparse
import sys

from pymatgen.io.vasp import Chgcar

from chgcomp.main_function import compress_isosurface, compress_isosurfaces


def parse_args(args):

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers()

    # -- compress_isosurface -------------------------------
    parser_compress_isosurface = subparsers.add_parser(
        name="compress_isosurface",
        description="compress CHGCAR to a single isosurface",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        aliases=['ci'])

    parser_compress_isosurface.add_argument("-c", "--chgcar", required=True,
                                            type=Chgcar.from_file)
    parser_compress_isosurface.add_argument("-l", "--level", default=0.5,
                                            type=float)
    parser_compress_isosurface.set_defaults(func=compress_isosurface)
    parser_compress_isosurface.add_argument("-s", "--suffix", default=None,
                                            help="suffix after output CHGCAR.")

    # -- compress_isosurfaces -------------------------------
    parser_compress_isosurfaces = subparsers.add_parser(
        name="compress_isosurfaces",
        description="compress a CHGCAR to 7 silces.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        aliases=['cis'])

    parser_compress_isosurfaces.add_argument("-c", "--chgcar", required=True,
                                             type=Chgcar.from_file)
    parser_compress_isosurfaces.set_defaults(func=compress_isosurfaces)

    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])
    args.func(args)


if __name__ == "__main__":
    main()


