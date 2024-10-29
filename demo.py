import sys
from news_project.logger import logging
from news_project.exception import ArticleException
from news_project.pipeline.data_ingestion_pipeline import DataIngestionPipeline 

def run_pipeline():
    """
    This method of TrainPipeline class is responsible for running complete pipeline
    """
    try:
        ingestion = DataIngestionPipeline()
        ingestion.main()

        


    except Exception as e:
        raise ArticleException(e, sys)


run_pipeline()