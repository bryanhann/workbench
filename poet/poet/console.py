#!/usr/bin/env python3
import sys
from pathlib import Path

import poet.upfind as UP
import poet.upfind.parser as PARSER

def upfind():
    print(123, sys.argv)
    args = PARSER.parser.parse_args(sys.argv[1:])
    start  =  Path(args.start).resolve()
    target = args.target
    try:
        found = UP.upfind( target, start )
        if args.full: found = found/target
        print( f'{found}' )
    except UP.UpfindException:
        sys.stderr.write('not found\n')
        sys.stdout.flush()
        return 1

#if __name__=='__main__':
#    main(sys.argv[1:])
