from the_parser.parser._EnvParser import EnvParser
from the_parser.preprocess._ConfigPreProcess import ConfigPreProcessor

from env import AVAILABLE_ENVS
from ext import AVAILABLE_EXTS

preprocessor = ConfigPreProcessor()
envparser = EnvParser(preprocessor)
envparser.injectdep(AVAILABLE_ENVS, AVAILABLE_EXTS)

CONFIG = envparser.all

__all__ = ['CONFIG']