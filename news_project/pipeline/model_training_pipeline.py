import sys
from news_project.exception import ArticleException
from news_project.logger import logging

from news_project.components.model_trainer import ModelTraining
from news_project.entity.config_entity import ModelTrainingConfig


class ModelTrainingPipeline:
    def __init__(self):
        self.model_training_config = ModelTrainingConfig()
    
        
    def main(self):
        """
        This method of ModelTrainPipeline class is responsible for starting model training component
        """
        try:
            model_training = ModelTraining(model_training_config=self.model_training_config)
            model_training.initiate_model_training()
        except Exception as e:
            raise ArticleException(e, sys)



#   For DVC Pipeline
if __name__ == '__main__':
    try:

        # Instantiate the pipeline components and pass the necessary configurations
        training = ModelTrainingPipeline()
        training.main()
        
    except Exception as e:
        raise e