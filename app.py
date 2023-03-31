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
from sklearn.ensemble import RandomForestClassifier

# generating object for the lemmatizer
wnl = WordNetLemmatizer()

# loading model and vectorizer....
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# preprocessing: remove stopwords, lemmatize, remove non-strings, vectorized the text, predict the output and return
def process(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.split()
    text = [wnl.lemmatize(word) for word in text if not word in stopwords.words('english')]
    text = ' '.join(text)

    text = vectorizer.transform([text]).toarray()
    result = model.predict(text)[0]
    return result

# Gradio interface
title = "News Articles Sorting"
interface = gr.Interface(fn=process,
                title = title,
                inputs=gr.inputs.Textbox(lines=20, placeholder='Insert the News Article'),
                outputs='text')
interface.launch(share=True)


