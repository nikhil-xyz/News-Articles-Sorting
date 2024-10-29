import sys

from news_project.exception import ArticleException
from news_project.logger import logging

import os
from news_project.constants import DATABASE_NAME, MONGODB_URI
import pymongo
import certifi

ca = certifi.where()

class MongoDBClient:
    """
    Class Name      :   export_data_into_feature_store
    Description     :   This method exports the dataframe from mongodb feature store as dataframe 

    parameters      : 
    database_name   :   Name of the database to connect to.
    
    Output          :   connection to mongodb database
    On Failure      :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URI)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URI} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")
        except Exception as e:
            raise LaptopException(e,sys)