import sys
import numpy as np
import pickle

from news_project.exception import ArticleException
from news_project.logger import logging
from news_project.configuration.azure_connection import BlobClient
from news_project.constants import CONTAINER_NAME, BLOB_NAME_MODEL, BLOB_NAME_TOKENIZER, PARAMS_FILE_PATH
from news_project.components.data_transformation import DataTransformation
from news_project.entity.config_entity import DataTransformationConfig, ModelTrainingConfig
from news_project.utils.main_utils import read_yaml_file, load_object
from tensorflow.keras.models import load_model

from tensorflow.keras.utils import pad_sequences
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from news_project.entity.estimator import TargetDecoding

class PredictionPipeline:
    def __init__(self):
        try:
            self.client = BlobClient()
            self.data_transformation_config = DataTransformationConfig()  
            self.data_transformation = DataTransformation(self.data_transformation_config)
            self.model_training_config = ModelTrainingConfig()
            self._param_config = read_yaml_file(file_path=PARAMS_FILE_PATH)
        except Exception as e:
            raise ArticleException(e, sys) from e

    def predict(self, article : str):
        try:
            # logging.info('Loading the tokenizer from Azure Blob')
            # tokenizer = self.client.get_binary_blob_data(CONTAINER_NAME, BLOB_NAME_TOKENIZER)
            # # converting byte format data to tokenizer
            # tokenizer = pickle.loads(tokenizer)

            # logging.info('Loading the model from Azure Blob')
            # model = self.client.get_binary_blob_data(CONTAINER_NAME, BLOB_NAME_MODEL)
            # # converting byte format data to '.h5' model
            # model = pickle.loads(model)

            # I have tried loading the model and the tokenizer from the azure container
            # But it was taking relatively long time to load
            # Code to load the model and the tokenizer from the container is available above
            # Now I am going with loading the model and the tokenizer from artifact files

            logging.info('Loading the model from artifact file')
            model = load_object(self.model_training_config.trained_model_file_path)

            logging.info('Loading the tokenizer from artifact file')
            tokenizer = load_object(self.data_transformation_config.transformed_object_file_path)

            logging.info('Cleaning and Transforming the input article')
            cleaned_article = self.data_transformation.data_cleaning(article)
            cleaned_article = self.data_transformation.padding_operations([cleaned_article], tokenizer, 2205)

            logging.info('Predicting the category of the article')
            prediction = model.predict([cleaned_article])
            prediction = np.argmax(prediction)

            # Converting the category number to category label
            decoding = TargetDecoding()
            return decoding.decode_target(prediction)


        except Exception as e:
            raise ArticleException(e, sys) from e


# article = "If the build-up to this game was all about Ruben Amorim and his impending move, much of the aftermath will be \
#     centred around Pep Guardiola and his team. The injury issues City are wrestling with meant Jahmai Simpson-Pusey was \
#     handed his first senior start in central defence, less than a week after his first-team debut. Simpson-Pusey only turned\
#     19 the day before the game and he was given a baptism of fire by hat-trick hero Viktor Gyokeres, who used all his experience\
#     to full effect. The City boss has said this season will be 'a struggle'. That prediction is already coming true. To help him\
#     out, he needs his senior players to have an impact. Phil Foden did so when he drove home his fourth goal of the season to \
#     set City on course for what seemed certain to be an easy win. But early chances to double the advantage came and went and \
#     City were swept away by two goals in four minutes at the start of the second half.Normally, a response would be expected.\
#     Had Erling Haaland converted his penalty, it might have come. The Norwegian has now failed to score in four of his last six\
#     games.It is not just City as a whole who are struggling, individual players are too."

# pipe = PredictionPipeline()
# result = pipe.predict(article)
# print(result)
