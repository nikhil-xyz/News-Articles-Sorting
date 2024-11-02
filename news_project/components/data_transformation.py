import re
import os
import sys
import string

import numpy as np
import pandas as pd

from news_project.exception import ArticleException
from news_project.logger import logging

from news_project.utils.main_utils import read_yaml_file, save_numpy_array_data, save_object
from news_project.constants import SCHEMA_FILE_PATH, PREDICTOR_FEATURE, TARGET_FEATURE, MAX_WORDS
from news_project.entity.config_entity import DataTransformationConfig

import nltk
nltk.download('punkt')

from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

import spacy
from spacy.cli import download
download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import pad_sequences

class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig):
        """
        arguments:
        data_transformation_config : Configuration for data transformation
        """
        try:
            self.data_transformation_config = data_transformation_config
            self._schema_config = read_yaml_file(file_path=SCHEMA_FILE_PATH)
        except Exception as e:
            raise ArticleException(e, sys)
        
    

    def target_encoding_operation(self, feature):
        """
        Method Name :   target_encoding_operation
        Description :   This method applies target encodings to the target feature of the training data
        
        Output      :   data is returned as artifact of data transformation components
        """        
        try:
            logging.info("Entered into the target encoding function")

            logging.info("Applying target encodings to the target feature of the training data")
            target_encodings = read_yaml_file(SCHEMA_FILE_PATH)
            feature = feature.map(target_encodings)
            
            logging.info(f"Exited target encoding")
            return feature

        except Exception as e:
            raise ArticleException(e,sys) from e
        
    

    def data_cleaning(self, text):
        """
        Method Name :   data_cleaning
        Description :   This method cleans the text data
        
        Input       :   text - a string
        Output      :   cleaned text as artifact of data transformation components
        """
        text = text.lower()
        text = re.sub(r'(\d+)m', r'\1 million ', text)  # 7.5m -> 7.5 million
        text = re.sub(r'(\d+)bn', r'\1 billion ', text)
        text = re.sub(r"(\d+),(\d+)", r"\1\2", text)  # 146,000 -> 146000
        text = re.sub(r'(\d+).(\d+)', ' number ', text) # 145 -> number
        text = re.sub(r'(\d+)', ' number ', text)

        # text = text.replace('gmt', ' greenwich mean time ')
        text = text.replace('\n', '').replace("\'s", "").replace("\'",' ')
        text = text.replace('$', ' dollar ').replace('£', ' euro ').replace('%', ' percent ')
        text = text.replace('"', '').replace('.','')

        # tokenization
        # we are using tokenizer from spacy, since nltk's is not working in vscode for the reason I don't know
        
        doc = nlp(text)
        tokens = [token.text for token in doc]

        # removing stopwords
        tokens = [token for token in tokens if token not in stop_words]

        # removing punctuations
        tokens = [token for token in tokens if token not in string.punctuation]

        # Lemmatization of tokens and joining them again to single string 
        lemmatizer = WordNetLemmatizer()
        lemmas = [lemmatizer.lemmatize(token) for token in tokens]
        sentence = ' '.join(lemmas)
        return sentence
        

    def generate_tokenizer(self, data):
        """
        Method Name :   generate_tokenizer
        Description :   This method generates a tokenizer from given data
        
        Input       :   data - a pandas series
        Output      :   tokenizer as artifact of data transformation components
        
        """
        tokenizer = Tokenizer(num_words = MAX_WORDS)
        tokenizer.fit_on_texts(data)

        return tokenizer


    def padding_operations(self, data, tokenizer, max_len): 
        """
        Method Name :   padding_operations
        Description :   This method applies padding operation to given data
        
        Input       :   data - a pandas series, tokenizer - a tokenizer, max_len - an integer
        Output      :   sequences_matrix as artifact of data transformation components
        """
        sequences = tokenizer.texts_to_sequences(data)
        sequences_matrix = pad_sequences(sequences, maxlen=max_len)
        return sequences_matrix
    

    def initiate_data_transformation(self):
        """
        This method of DataTransformation class is responsible for initiating data transformation component
        """
        try:
            logging.info("Entered the initiate_data_transformation method of Data transformation class")
               
            training_data = pd.read_csv(self.data_transformation_config.training_file_path)
            testing_data = pd.read_csv(self.data_transformation_config.testing_file_path)

            logging.info("Seperating Predictor and Target features from training and testing data")
            train_x = training_data[PREDICTOR_FEATURE]
            train_y = training_data[TARGET_FEATURE]
            test_x = testing_data[PREDICTOR_FEATURE]
            test_y = testing_data[TARGET_FEATURE]

            logging.info("Applying target encodings to both training and testing data")
            train_y = self.target_encoding_operation(train_y)
            test_y = self.target_encoding_operation(test_y)

            logging.info("Applying data cleaning to the predictor feature of the training data")
            train_x = train_x.apply(self.data_cleaning)
            test_x = test_x.apply(self.data_cleaning)

            logging.info("Calculating length of longest sentence from training and testing set")
            max_len_train = max(train_x.apply(lambda x: len(x.split())))
            max_len_test = max(test_x.apply(lambda x: len(x.split())))
            max_len = max(max_len_train, max_len_test)

            logging.info("Generating Tokenizer using training data")
            tokenizer = self.generate_tokenizer(train_x)

            logging.info("Applying tokenizer and padding operation to data")
            train_x = self.padding_operations(train_x, tokenizer, max_len)
            test_x = self.padding_operations(test_x, tokenizer, max_len)
            

            logging.info("Storing preprocessed training and testing data to artifacts")
            os.makedirs(self.data_transformation_config.data_transformation_dir, exist_ok=True)
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path, array=train_x)
            save_numpy_array_data(self.data_transformation_config.transformed_train_label_path, array=train_y)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path, array=test_x)
            save_numpy_array_data(self.data_transformation_config.transformed_test_label_path, array=test_y)

            logging.info("Storing the tokenizer into artifacts")
            save_object(self.data_transformation_config.transformed_object_file_path, tokenizer)
            logging.info("Exited the initiate_data_transformation method of Data transformation class")

       
        except Exception as e:
            raise ArticleException(e, sys) from e