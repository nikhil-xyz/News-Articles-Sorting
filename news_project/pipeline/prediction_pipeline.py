import sys
import numpy as np

from news_project.exception import ArticleException
from news_project.logger import logging
from news_project.configuration.azure_connection import BlobClient
from news_project.constants import CONTAINER_NAME, BLOB_NAME_MODEL, BLOB_NAME_TOKENIZER, PARAMS_FILE_PATH
from news_project.components.data_transformation import DataTransformation
from news_project.entity.config_entity import DataTransformationConfig
from news_project.utils.main_utils import read_yaml_file

from tensorflow.keras.utils import pad_sequences
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class PredictionPipeline:
    def __init__(self):
        try:
            self.client = BlobClient()
            self.data_transformation_config = DataTransformationConfig()  
            self.data_transformation = DataTransformation(self.data_transformation_config)
            self._param_config = read_yaml_file(file_path=PARAMS_FILE_PATH)
        except Exception as e:
            raise ArticleException(e, sys) from e

    def predict(self, article : str):
        try:
            logging.info('Loading the tokenizer from Azure Blob')
            tokenizer = self.client.get_binary_blob_data(CONTAINER_NAME, BLOB_NAME_TOKENIZER)

            logging.info('Loading the model from Azure Blob')
            model = self.client.get_binary_blob_data(CONTAINER_NAME, BLOB_NAME_MODEL)

            logging.info('Cleaning and Transforming the input article')
            cleaned_article = self.data_transformation.data_cleaning(article)
            cleaned_article = self.data_transformation.padding_operations(cleaned_article, tokenizer, 2205)

            logging.info('Predicting the category of the article')
            prediction = model.predict(cleaned_article)
            prediction = np.argmax(prediction)

            return prediction


        except Exception as e:
            raise ArticleException(e, sys) from e


article = "Voting for the U.S. Presidential elections is set to take place today, and both candidates have been campaigning \
tirelessly to claim the top spot. Many political observers billed the unpredictable race for the 47th President of \
the US as the most consequential one in decades while appearing to project a grim picture for the country’s future under \
a Trump presidency. Also Read | Trump, Harris focus on ‘Blue Wall’ States in the final hours of the campaign \
In her closing remarks in her Michigan rally on Sunday, Kamala Harris sought to strike on an optimistic note, saying \
that the U.S. had an opportunity for a fresh start and could turn the page on a decade of politics driven by fear and \
ivision. Donald Trump focused on the security of the U.S.-Mexico border, attacking Democrats and saying he will improve \
the economy, during his closing arguments in Raleigh, North Carolina on Monday.Also Read U.S. Presidential elections 2024: \
Key dates and events to note An early voting station was set up at the John Jay College in the Manhattan area of NYC. Voters \
flocked the read and cast their ballots days ahead of the main election day on November 5. Suzan, the coordinator of \
the station, said the early voting process is witnessing a very positive response."

pipe = PredictionPipeline()
result = pipe.predict(article)
print(result)