#!/usr/bin/env python3
from pathlib import Path

class UpfindException(Exception):
    pass

def upfind(target,folder):
    folder=Path(folder)
    if (folder/target).exists():
        return folder
    if not (folder==folder.parent):
        return upfind(target, folder.parent)
    raise UpfindException('not found')

