import os
from news_project.constants import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP:str = datetime.now().strftime('%d-%m-%Y-%H-%M')

@dataclass
class TrainingPipelineConfig:
    """
    Configures the training pipeline.

    Attributes:
    pipeline_name (str) : Name of the training pipeline.
    artifact_dir (str)  : Directory to store the artifacts of the training pipeline.
    timestamp (str)     : Timestamp for the training pipeline. Will play role in the artifact naming.
    """
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = os.path.join(ARTIFACT_DIR)
    # artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP) for the version control
    timestamp: str = TIMESTAMP


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()


@dataclass
class DataIngestionConfig:
    """
    Configures the data ingestion process.

    Attributes:
    data_ingestion_dir (str)        : Directory to store the ingested data.
    feature_store_file_path (str)   : Path to the feature store file containing the ingested data.
    training_file_path (str)        : Path to the training file containing the ingested data.
    test_file_path (str)            : Path to the test file containing the ingest data.
    train_test_split_ratio (float)  : Ratio of training data to test data.
    collection_name (str)           : Name of the MongoDB collection containing the ingested data.
    """
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
    testing_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name:str = DATA_INGESTION_COLLECTION_NAME


@dataclass
class DataTransformationConfig:
    """
    Configures the data transformation process.
    
    Attributes:
    data_ingestion_dir (str)        : Directory to store the ingested data.
    training_file_path (str)        : Path to the training file containing the ingested data.
    test_file_path (str)            : Path to the test file containing the ingest data.
    
    data_transformation_dir (str)      : Directory to store the data transformation artifacts.
    transformed_train_file_path (str)  : Path to the transformed training file containing the preprocessed data.
    transformed_test_file_path (str)   : Path to the transformed test file containing the preprocessed data.
    transformed_object_file_path (str) : Path to the object file containing the preprocessing transformations.
    """
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
    testing_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)

    data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_TRANSFORMATION_DIR_NAME)
    transformed_train_file_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                    TRANSFORMED_TRAIN_FILE_NAME)
    transformed_train_label_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                    TRANSFORMED_TRAIN_LABEL_NAME)
    transformed_test_file_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                   TRANSFORMED_TEST_FILE_NAME)
    transformed_test_label_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                   TRANSFORMED_TEST_LABEL_NAME)                                               
    transformed_object_file_path: str = os.path.join(data_transformation_dir,
                                                     DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
                                                     TOKENIZER_OBJECT_FILE_NAME)

    

@dataclass
class ModelTrainingConfig:
    data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_TRANSFORMATION_DIR_NAME)
    transformed_train_file_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                    TRANSFORMED_TRAIN_FILE_NAME)
    transformed_train_label_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                    TRANSFORMED_TRAIN_LABEL_NAME)
    transformed_object_file_path: str = os.path.join(data_transformation_dir,
                                                     DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
                                                     TOKENIZER_OBJECT_FILE_NAME)


    model_trainer_dir: str = os.path.join(training_pipeline_config.artifact_dir, MODEL_TRAINER_DIR_NAME)
    trained_model_file_path: str = os.path.join(model_trainer_dir, MODEL_TRAINER_TRAINED_MODEL_DIR, MODEL_TRAINER_TRAINED_MODEL_NAME)


@dataclass
class ModelEvaluationConfig:
    data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_TRANSFORMATION_DIR_NAME)
    transformed_test_file_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                    TRANSFORMED_TRAIN_FILE_NAME)
    transformed_test_label_path: str = os.path.join(data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                    TRANSFORMED_TRAIN_LABEL_NAME)
    transformed_object_file_path: str = os.path.join(data_transformation_dir,
                                                     DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
                                                     TOKENIZER_OBJECT_FILE_NAME)

    model_trainer_dir: str = os.path.join(training_pipeline_config.artifact_dir, MODEL_TRAINER_DIR_NAME)
    trained_model_file_path: str = os.path.join(model_trainer_dir, MODEL_TRAINER_TRAINED_MODEL_DIR, MODEL_TRAINER_TRAINED_MODEL_NAME)