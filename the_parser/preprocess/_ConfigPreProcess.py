from the_parser.base._PreProcess import PreProcessor

from termcolor import colored

class ConfigPreProcessor(PreProcessor):
    def preprocess(self, object: dict) -> dict:
        try:
            splitinputpath = str(object['INPUT_PATH']).split(',')
            object['INPUT_PATH'] = splitinputpath

        except KeyError as e:
            print(colored(f"Object must have {e} keyword. Returning raw object.", 'red'))

        finally:
            return object
    
if __name__ == "__main__":
    envs = {
        'INPUT_PAT': 'C:/Coding_folder/Python/search/Container/benigns,C:/Coding_folder/Python/search/Container/malwares/thisisbenign.exe,C:/Coding_folder/Python/search/Container/malwares'
    }
    
    the_parserpreprocess = ConfigPreProcessor()
    envs = the_parserpreprocess.preprocess(envs)