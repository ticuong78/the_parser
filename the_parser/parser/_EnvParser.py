import os
import dotenv as de

from the_parser.base._Parser import Parser
from the_parser.base._PreProcess import PreProcessor

from typing import List

de.load_dotenv(override=True)

class EnvParser(Parser):
    def injectdep(self, available_envs: List[str], available_exts: List[str]):
        """
            Params:
            ---------
            ``available_envs``: list of strings that contains many environmental variables that are currently supported or are meaningful to your program.
            
            ``available_exts``: list of strings indicates many extensions supported by your program. As this project is specifically built for the Analyse Malware using FFT project (mentioned in README.md of https://github.com/ticuong78/Analyse-Malware-using-FFT) so it may make no sense in your project.
            
            Returns:
            ---------
            None: set variables for EnvParser object
        """

        self._available_exts = available_exts
        self._available_envs = available_envs

    @property
    def all(self):
        if self._available_exts is None or self._available_envs is None:
            raise ValueError("Use EnvParser.injectdep() to firstly set the parser's dependent variables.")

        object = self._preprocessor.preprocess(self._parse())
        object['EXTENSIONS'] = self._available_exts

        return object

    def __init__(self, preprocessor: PreProcessor):
        self._preprocessor = preprocessor

    def _parse(self):
        envs = dict([(env, os.getenv(env)) for env in self._available_envs])

        return envs