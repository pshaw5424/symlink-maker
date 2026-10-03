"""Symlink Maker — Create Windows directory junctions and file links with a path preview."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='symlink_maker',
        description='Create Windows directory junctions and file links with a path preview.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Symlink Maker')
    print('Junctions and symlinks without mklink flags you forget.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
