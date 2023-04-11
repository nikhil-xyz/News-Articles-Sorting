# importing dependencies
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
import gradio as gr
import logging

# initializing logging
logging.basicConfig(filename='logs.log',
                    filemode='a',
                    format='%(asctime)s %(levelname)s - %(message)s)',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)

# generating object for the lemmatizer
try:
    wnl = WordNetLemmatizer()
except:
    logging.debug("Problem while invoking WordNetLemmatizer object")

# loading model and vectorizer....
try:
    model = pickle.load(open('model.pkl', 'rb'))
    vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
except:
    logging.debug("Problem while loading pickle files")

# preprocessing: remove stopwords, lemmatize, remove non-strings, vectorized the text, predict the output and return
def process(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.split()
    text = [wnl.lemmatize(word) for word in text if not word in stopwords.words('english')]
    text = ' '.join(text)
    try:
        text = vectorizer.transform([text]).toarray()
        result = model.predict(text)[0]
    except:
        logging.debug("Problem while vectorization and prediction")
    return result

# Gradio interface
title = "News Articles Sorting"
interface = gr.Interface(fn=process,
                title = title,
                inputs=gr.inputs.Textbox(lines=20, placeholder='Insert the News Article'),
                outputs='text')
interface.launch(server_name="0.0.0.0", server_port=7860)


