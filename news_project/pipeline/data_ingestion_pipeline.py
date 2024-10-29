import sys
from news_project.exception import ArticleException
from news_project.logger import logging

from news_project.components.data_ingestion import DataIngestion


from news_project.entity.config_entity import DataIngestionConfig
# from news_project.entity.artifact_entity import DataIngestionArtifact


class DataIngestionPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        
    def main(self):
        """
        This method of TrainPipeline class is responsible for starting data ingestion component
        """
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)
            data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info(
                "Exited the start_data_ingestion method of DataIngestionPipeline class"
            )
            
        except Exception as e:
            raise ArticleException(e, sys) from e


if __name__ == '__main__':
    try:
        obj = DataIngestionPipeline()
        obj.main()
        
    except Exception as e:
        raise e