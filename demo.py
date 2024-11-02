import sys
from news_project.logger import logging
from news_project.exception import ArticleException
from news_project.pipeline.data_ingestion_pipeline import DataIngestionPipeline 
from news_project.pipeline.data_transformation_pipeline import DataTransformationPipeline
from news_project.pipeline.model_training_pipeline import ModelTrainingPipeline

def run_pipeline():
    """
    This method of TrainPipeline class is responsible for running complete pipeline
    """
    try:
        ingestion = DataIngestionPipeline()
        ingestion.main()

        transformation = DataTransformationPipeline()
        transformation.main()

        training = ModelTrainingPipeline()
        training.main()


    except Exception as e:
        raise ArticleException(e, sys)


run_pipeline()