import sys

from news_project.logger import logging
from news_project.exception import ArticleException
from news_project.entity.config_entity import ModelTrainingConfig
from news_project.utils.main_utils import load_numpy_array_data, load_object, read_yaml_file, save_object
from news_project.rnn_architecture.model import Model_Architecture
from news_project.constants import PARAMS_FILE_PATH

class ModelTraining:
    def __init__(self, model_training_config: ModelTrainingConfig):
        """
        Arguments:
        model_training_config : Configuration for model training
        """
        try:
            self.model_training_config = model_training_config
            self._param_config = read_yaml_file(file_path=PARAMS_FILE_PATH)
        except Exception as e:
            raise ArticleException(f'Error while initializing ModelTraining: {str(e)}', sys)



    def get_training_data(self):
        """
        Method Name :   get_training_data
        Description :   This method retrieves the training data from the specified file paths
        
        Returns:
        train_x     : Numpy array containing the training data features
        train_y     : Numpy array containing the training data labels
        tokenizer   : Tokenizer object used for text preprocessing
        """
        
        train_x = load_numpy_array_data(self.model_training_config.transformed_train_file_path)
        train_y = load_numpy_array_data(self.model_training_config.transformed_train_label_path)
        tokenizer = load_object(self.model_training_config.transformed_object_file_path)

        return train_x, train_y, tokenizer


    def train_model(self, train_x, train_y, tokenizer):
        """
        Method Name :   train_model
        Description :   This method trains the model using the provided training data
        
        Arguments:
        train_x     : Numpy array containing the training data features
        train_y     : Numpy array containing the training data labels
        tokenizer   : Tokenizer object used for text preprocessing
        
        Returns:
        model      : Trained model
        """
        logging.info('Retrieving RNN Architecture')
        model_architecture = Model_Architecture()

        logging.info('Setting up training parameters')
        model = model_architecture.get_rnn_architecture()

        logging.info('Training the model')
        model.fit(train_x, train_y, epochs=self._param_config['EPOCH'], batch_size=self._param_config['BATCH_SIZE'],
                                                validation_split=self._param_config['VALIDATION_SPLIT'])

        return model
    


    def initiate_model_training(self,):
        """
        Method Name :   initiate_model_trainer
        Description :   This method initiates the model training components of training pipeline
        """
        logging.info('Entered initiate_model_trainer method of ModelTraining class')
        logging.info('Retrieving training data and tokenizer')
        train_x, train_y, tokenizer = self.get_training_data()

        logging.info('Training the model')
        train_model = self.train_model(train_x, train_y, tokenizer)

        logging.info('Storing the trained model')
        save_object(self.model_training_config.trained_model_file_path, train_model)

        logging.info('Exited initiate_model_trainer method of ModelTraining class')
