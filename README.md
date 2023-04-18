
# Machine Learning project on News articles sorting with gradio

A fully functional EXAMPLE project written in Python showing how to write classification model and deploy using Hugging Face.  







## Demo

https://github.com/nikhil-xyz/News-Articles-Sorting/blob/main/ezgif.com-optimize.gif


## Roadmap

- Kaggle Dataset https://www.kaggle.com/c/learn-ai-bbc/data

- The trained model can be picked using pickle
    - install picke : pip install pickle5
    - dump pickle : pickle.dump(model_name, open('model.pkl','wb'))
    - load model : model = pickle.load(open('model.pkl', 'rb'))
- Use the same strategy for vectorizer




## Usage/Examples

- gradio interface

    interface = gradio.Interface(fn=/* preprocessing function */,

                    title = /* title-string */,

                    inputs=gradio.inputs.Textbox(lines=#),

                    outputs='text')

    interface.launch(server_name="0.0.0.0", server_port=7860)
    
- The 'fn' parameter will specify the the fuction where input data
  will be preprocessed.
- The default port used by Hugging Face is 7860.



## Deployment

- To run the interface on different OS, it should be containerized.
- The root user could cause permission issues, non-root user
  should be used.

  RUN useradd -m -u 1000 user
  USER user

- Set home to the user's home directory

    ENV HOME=/home/user \
	    PATH=/home/user/.local/bin:$PATH

    WORKDIR $HOME/app

- Copy the current directory contents into the container at $HOME/
  app setting the owner to the user

    COPY --chown=user . $HOME/app

    ADD --chown=user ./. $HOME/app/.

    RUN chown user:user -R $HOME/app

    COPY ./requirements.txt /code/requirements.txt

- Execution

    RUN pip install --no-cache-dir --upgrade -r /code/      
    requirements.txt

    CMD ["python", "app.py"]
 


