import sys
from news_project.exception import ArticleException
from news_project.logger import logging

from news_project.components.model_pusher import ModelPusher
from news_project.entity.config_entity import ModelPusherConfig



class ModelPusherPipeline:
    def __init__(self):
        self.model_pusher_config = ModelPusherConfig()
        
    def main(self):
        """
        This method of ModelPusherPipeline class is responsible for pushing the model to azure blob
        """
        try:
            model_pusher = ModelPusher(model_pusher_config = self.model_pusher_config)
            model_pusher.initiate_model_pusher()
            
        except Exception as e:
            raise ArticleException(e, sys) from e


if __name__ == '__main__':
    try:
        obj = ModelPusherPipeline()
        obj.main()
        
    except Exception as e:
        raise e