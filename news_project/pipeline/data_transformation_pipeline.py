import sys
from news_project.exception import ArticleException
from news_project.logger import logging

from news_project.components.data_transformation import DataTransformation
from news_project.entity.config_entity import DataTransformationConfig


class DataTransformationPipeline:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
        
    def main(self):
        """
        This method of TrainPipeline class is responsible for starting data transformation component
        """
        try:
            data_transformation = DataTransformation(data_transformation_config=self.data_transformation_config)
            data_transformation.initiate_data_transformation()
        except Exception as e:
            raise ArticleException(e, sys)



#   For DVC Pipeline
if __name__ == '__main__':
    try:

        # Instantiate the pipeline components and pass the necessary configurations
        transformation = DataTransformationPipeline()
        transformation.main()
        
    except Exception as e:
        raise e