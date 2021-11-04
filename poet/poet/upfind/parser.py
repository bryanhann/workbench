#!/usr/bin/env python3

from pathlib import Path
import sys

if 1:
    import argparse
    parser = argparse.ArgumentParser(
        prog=f"\n\t{Path(sys.argv[0]).name.upper()}"
        , description = "Upfind a target"
        , formatter_class=argparse.RawDescriptionHelpFormatter
        , epilog="""This is a raw epilog."""
    )

    parser.add_argument(
        "--start"
        , "-s"
        , help="start searching here"
        , default=Path.cwd()
        )

    parser.add_argument(
        "--full"
        , "-f"
        , action='store_true'
        , help="full path, including target"
        )

    parser.add_argument(
        "target"
        , help="the object to search for"
        )


