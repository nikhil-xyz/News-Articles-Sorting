import sys
from news_project.logger import logging
from news_project.exception import ArticleException
from news_project.pipeline.data_ingestion_pipeline import DataIngestionPipeline 
from news_project.pipeline.data_transformation_pipeline import DataTransformationPipeline
from news_project.pipeline.model_training_pipeline import ModelTrainingPipeline
from news_project.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
from news_project.pipeline.model_pusher_pipeline import ModelPusherPipeline

def run_pipeline():
    """
    This method of TrainPipeline class is responsible for running complete pipeline
    """
    try:
        # Running the Ingestion Module
        ingestion = DataIngestionPipeline()
        ingestion.main()

        # Running the Transformation Module 
        transformation = DataTransformationPipeline()
        transformation.main()

        # Running the Model Training Module
        training = ModelTrainingPipeline()
        training.main()

        # Running the Model Evaluation Module  
        evaluation = ModelEvaluationPipeline()
        evaluation.main()

        # Pushing the Model
        pusher = ModelPusherPipeline()
        pusher.main()


    except Exception as e:
        raise ArticleException(e, sys)


run_pipeline()