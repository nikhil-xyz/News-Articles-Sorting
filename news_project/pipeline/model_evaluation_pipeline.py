import sys
from news_project.exception import ArticleException
from news_project.logger import logging

from news_project.components.model_evaluation_mlflow import ModelEvaluation
from news_project.entity.config_entity import ModelEvaluationConfig


class ModelEvaluationPipeline:
    def __init__(self):
        self.model_evaluation_config = ModelEvaluationConfig()
    
        
    def main(self):
        """
        This method of ModelEvaluationPipeline class is responsible for starting model evaluation component
        """
        try:
            model_evaluation = ModelEvaluation(model_evaluation_config=self.model_evaluation_config)
            model_evaluation.initiate_model_evaluation()
        except Exception as e:
            raise ArticleException(e, sys)



#   For DVC Pipeline
if __name__ == '__main__':
    try:

        # Instantiate the pipeline components and pass the necessary configurations
        evaluation = ModelEvaluationPipeline()
        evaluation.main()
        
    except Exception as e:
        raise e