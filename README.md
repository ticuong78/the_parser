# The parser

This is a sub-project of the [Analyse Malware using FFT](https://github.com/ticuong78/Analyse-Malware-using-FFT)

## Description

This project helps its user find and parse any environmental variables with EnvParser class. Furthermore, it also supports applying any preprocess functions by passing an inherited class of the PreProcess base class into its constructor.

## Example

### With PreProcess sub classes

<div font-family="monospace">
    from the_parser.parser._EnvParser import EnvParser
    from the_parser.preprocess._ConfigPreProcess import ConfigPreProcessor

    from _env import AVAILABLE_ENVS
    from _ext import AVAILABLE_EXTS

    preprocessor = ConfigPreProcessor()
    envparser = EnvParser(preprocessor)
    envparser.injectdep(AVAILABLE_ENVS, AVAILABLE_EXTS)

    CONFIG = envparser.all

    __all__ = ['CONFIG']
</div>

### Without PreProcess sub classes

<div font-family="monospace">
    from the_parser.parser._EnvParser import EnvParser
    from the_parser.preprocess._ConfigPreProcess import ConfigPreProcessor

    from _env import AVAILABLE_ENVS
    from _ext import AVAILABLE_EXTS

    envparser = EnvParser()
    envparser.injectdep(AVAILABLE_ENVS, AVAILABLE_EXTS)

    CONFIG = envparser.all

    __all__ = ['CONFIG']
</div>
