import sys
from news_project.logger import logging
from news_project.exception import ArticleException
from news_project.utils.main_utils import read_yaml_file
from news_project.constants import SCHEMA_FILE_PATH

class TargetDecoding:
    def __init__(self):
        """
        Initializes the target decoding component with the provided configuration path.
        """
        try:
            self.dictionary = read_yaml_file(file_path=SCHEMA_FILE_PATH)
            
        except Exception as e:
            raise ArticleException(f'Error while initializing TargetDecoding: {str(e)}', sys)

    def decode_target(self, target_value):
        """
        Decodes the target value from its encoded form to its human-readable form.
        
        Args:
            target_value (int): The encoded target value.
        """
        try:
            logging.info('Decoding the target value, returining the key associated with it.')
            for key, val in self.dictionary.items():
                if val == target_value:
                    return key
        except Exception as e:
            raise ArticleException(f'Error while decoding target value: {str(e)}', sys) from e
    

