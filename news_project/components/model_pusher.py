import sys
from news_project.logger import logging
from news_project.exception import ArticleException

from news_project.entity.config_entity import ModelPusherConfig
from news_project.configuration.azure_connection import BlobClient
from news_project.constants import CONTAINER_NAME


class ModelPusher:
    def __init__(self, model_pusher_config: ModelPusherConfig = ModelPusherConfig()):
        try:
            self.model_pusher_config = model_pusher_config
            self.client = BlobClient()
            self.container_name = CONTAINER_NAME
        except Exception as e:
            raise ArticleException(e, sys) from e
    
    def push_model_and_tokenizer_to_azure(self):
        """
        Method Name :   push_model_and_tokenizer_to_azure
        Description :   This method uploads the trained model and tokenizer object to Azure Blob Storage
        """
        try:
            logging.info('Pushing model to Azure Blob Storage...')
            model_path = self.model_pusher_config.trained_model_file_path
            self.client.upload_blob(model_path, self.container_name)

            logging.info('Pushing tokenizer object to Azure Blob Storage...')
            tokenizer_path = self.model_pusher_config.transformed_object_file_path
            self.client.upload_blob(tokenizer_path, self.container_name)

        except Exception as e:
            raise ArticleException(e, sys) from e


    def initiate_model_pusher(self):
        """
        Method Name :   initiate_model_pusher
        Description :   This method initiates the model pushing process
        """
        try:
            logging.info('Entered initiate_model_pusher method of ModelPusher class')
            self.push_model_and_tokenizer_to_azure()
            logging.info('Exited initiate_model_pusher method of ModelPusher class')

        except Exception as e:
            raise ArticleException(e, sys) from e