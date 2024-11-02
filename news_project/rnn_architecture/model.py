from news_project.logger import logging
from news_project.exception import ArticleException
from news_project.utils.main_utils import read_yaml_file
from news_project.constants import PARAMS_FILE_PATH

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Embedding, Bidirectional
# from tensorflow.keras.optimizers import RMSprop
# from tensorflow.keras.callbacks import EarlyStopping
from PIL import Image, ImageDraw, ImageFont

class Model_Architecture:
    def __init__(self):
        self._param_config = read_yaml_file(file_path=PARAMS_FILE_PATH)

    def get_image_summary(self):
        """
        This function will be responsible for covnerting '.txt' file 
        containing the model summary into the '.png' file
        """
        # Open the text file
        with open('model_summary.txt', 'r') as f:
            text = f.read()

        # Create an image
        img = Image.new('RGB', (600, 400), (255, 255, 255))  # Adjust size as needed
        draw = ImageDraw.Draw(img)

        # Choose a font
        font = ImageFont.truetype("arial.ttf", 20)  # Adjust font and size

        # Draw the text on the image
        draw.text((10, 10), text, font=font, fill=(0, 0, 0))

        # Save the image
        img.save('model_summary.png')


    def get_rnn_architecture(self):
        """
        This function will create the RNN architecture for the news articles sorting model
        """
        model = Sequential()
        # Create the embedding layer
        model.add(Embedding(self._param_config['MAX_WORDS'], self._param_config['EMBEDDING_SIZE']))
        # Bidirectional LSTM Layer
        model.add(Bidirectional(LSTM(self._param_config['LSTM_NODES'], activation='tanh')))
        # Feature extractor Fully connected layers
        # model.add(Dense(self._param_config['DENSE_NODES'], activation='relu'))
        # Final layer
        model.add(Dense(5, activation='sigmoid'))
        model.compile(loss='sparse_categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])

        # Storing model summary inside the .txt file
        # summary = model.summary()
        summary_file = 'model_summary.txt'
        with open(summary_file, 'w') as f:
            model.summary(print_fn=lambda x: f.write(x + '\n'))

        # Storing model summary inside the png image
    
        self.get_image_summary()

        return model