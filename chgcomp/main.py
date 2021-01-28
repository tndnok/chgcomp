# coding: utf-8
#  Copyright (c) 2020 Kumagai group.

import argparse
import sys

from pymatgen.io.vasp import Chgcar

from chgcomp.main_function import compress_isosurface, decompress_isosurface, \
    compress_isosurfaces, decompress_isosurfaces


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

    # -- decompress_isosurface -------------------------------
    parser_decompress_isosurface = subparsers.add_parser(
        name="decompress_isosurface",
        description="decompress a single isosurface",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        aliases=['di'])

    parser_decompress_isosurface.add_argument("-i", "--isurf", required=True,
                                              type=str)
    parser_decompress_isosurface.add_argument("-s", "--suffix", default=None,
                                              help="suffix after output CHGCAR.")
    parser_decompress_isosurface.set_defaults(func=decompress_isosurface)

    # -- compress_isosurfaces -------------------------------
    parser_compress_isosurfaces = subparsers.add_parser(
        name="compress_isosurfaces",
        description="compress a CHGCAR to 7 silces.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        aliases=['cis'])

    parser_compress_isosurfaces.add_argument("-c", "--chgcar", required=True,
                                             type=Chgcar.from_file)
    # parser_compress_isosurfaces.add_argument("-s", "--slice", default=8, type=int,
    #                                        help="8 or 16")
    parser_compress_isosurfaces.set_defaults(func=compress_isosurfaces)

    # -- decompress_isosurfaces -------------------------------
    parser_decompress_isosurfaces = subparsers.add_parser(
        name="decompress_isosurfaces",
        description="decompress slices to 7 CHGCARs",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        aliases=['dis'])

    parser_decompress_isosurfaces.add_argument("-i", "--isurf", required=True,
                                               type=str)
    parser_decompress_isosurfaces.set_defaults(func=decompress_isosurfaces)

    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])
    args.func(args)


if __name__ == "__main__":
    main()


