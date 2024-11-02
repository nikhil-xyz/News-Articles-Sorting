import sys
import mlflow
import numpy as np
from news_project.logger import logging
from news_project.exception import ArticleException
from news_project.entity.config_entity import ModelEvaluationConfig
from news_project.utils.main_utils import load_numpy_array_data, load_object, save_object, read_yaml_file
from news_project.constants import PARAMS_FILE_PATH

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import dagshub
dagshub.init(repo_owner='nikhil.sonkusare94', repo_name='News-Articles-Sorting', mlflow=True)


class ModelEvaluation:
    def __init__(self, model_evaluation_config: ModelEvaluationConfig):
        try:
            self.model_evaluation_config = model_evaluation_config
            self._param_config = read_yaml_file(file_path=PARAMS_FILE_PATH)
        except Exception as e:
            raise ArticleException(e, sys) from e

    def evaluate_model(self, trained_model, test_x, test_y):
        """
        Method Name :   evaluate_model
        Description :   This method evaluates the model's performance on the test data
        
        Arguments:
        model      :   trained model
        test_x     :   test data features
        test_y     :   test data labels
        """

        with mlflow.start_run():
            logging.info('Making predictions for testing data')
            lstm_prediction = trained_model.predict(test_x)

            # Converting the predictions to labels
            # Assuming the model predicts the class label with the highest probability as the prediction
            # This is a simple implementation and may not be accurate for all models and datasets
            # For more complex models, you may need to use a different approach to convert the predictions to labels
            # For example, if the model is a multi-class classifier, you can use the 'predict_proba' method to get the probabilities for each class
            # Then, you can choose the class with the highest probability as the prediction
            # Example: pred = np.argmax(lstm_prediction, axis=1)

            # Alternatively, you can use a threshold to convert probabilities to labels
            # Example: pred = [1 if prob > 0.5 else 0 for prob in lstm_prediction
            pred = []
            for prediction in lstm_prediction:
                pred.append(np.argmax(prediction))

            logging.info('Calculating performance metrics')
            accuracy = accuracy_score(test_y, pred)
            precision = precision_score(test_y, pred, average='weighted')  # Use 'weighted' for multi-class
            recall = recall_score(test_y, pred, average='weighted')
            f1 = f1_score(test_y, pred, average='weighted')

            logging.info('logging matrics and parameters used in testing to mlflow for further evaluation')
            mlflow.log_params(self._param_config)
            mlflow.log_metric('accuracy', accuracy)
            mlflow.log_metric('precision', precision)
            mlflow.log_metric('recall', recall)
            mlflow.log_metric('f1_score', f1)
          
        logging.info(f"Performance Metric \nAccuracy: {accuracy}\nPrecision: {precision}\nRecall: {recall}\nF1_score: {f1}")


    def initiate_model_evaluation(self):
        """
        Method Name :   initiate_model_evaluation
        Description :   This method initiates the model evaluation process
        """
        try:
            logging.info('Entered initiate_model_trainer method of ModelEvaluation class')
            
            logging.info("Loading the model from artifacts")
            model = load_object(self.model_evaluation_config.trained_model_file_path)
            
            # logging.info('Loading the tokenizer object from artifacts')
            # tokenizer = load_object(self.model_evaluation_config.transformed_object_file_path)

            logging.info('Loading the test data')
            test_x = load_numpy_array_data(self.model_evaluation_config.transformed_test_file_path)
            test_y = load_numpy_array_data(self.model_evaluation_config.transformed_test_label_path)
            self.evaluate_model(model, test_x, test_y)

            logging.info('Exited initiate_model_trainer method of ModelEvaluation class')


        except Exception as e:
            raise ArticleException(e, sys) from e
