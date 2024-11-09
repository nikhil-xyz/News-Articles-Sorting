import os
import sys
import gradio as gr

from news_project.logger import logging
from news_project.exception import ArticleException
from news_project.pipeline.prediction_pipeline import PredictionPipeline


# Check if the model has been trained before launching the application
if not os.path.isdir('artifact'):
    logging.info('Executing python main.py')
    os.system('python main.py')

obj = PredictionPipeline()
def prediction(article):
    """
    This function takes a news article as input and returns the predicted category.
    """
    try:
        result = obj.predict(article)
        return result
    except Exception as e:
        raise ArticleException(e, sys) from e


# creating user interface
interface = gr.Interface(fn=prediction, 
                         inputs=gr.Textbox(lines=20, placeholder='Post a news article here'),
                         outputs='label',
                         title="News Articles Sorting",
                         css=".gr-title {text-align: center; font-family: 'Times New Roman', serif; font-size: 36px;}")


interface.launch()