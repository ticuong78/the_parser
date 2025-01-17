import os
import json as js

from os import PathLike
from typing import Union
from pathlib import Path
from the_parser.base._Parser import Parser

class ParamParser(Parser):
    def __init__(self, path: Union[PathLike, Path, str]):
        self.json_obj = self._parse(path)

    def _parse(self, path: Union[PathLike, Path, str]) -> dict:
        internalPath = str(path)

        if not os.path.exists(internalPath):
            raise ValueError("File does not exists.")
        
        if not os.path.splitext(internalPath)[1]:
            raise TypeError("Path must be a link to a file.")

        with open(internalPath, "r") as f:
            json_obj = js.loads(f.read())

        return json_obj