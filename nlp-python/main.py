# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import vertexai
from vertexai.language_models import TextGenerationModel
from transformers import pipeline

import os

from flask import Flask, request

from models import SentimentAnalysisEntity, TopicModellingEntity

app = Flask(__name__)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.expanduser(
    '~/.config/gcloud/application_default_credentials.json')


@app.route('/health')
def health():
    return {
        "status": "UP"
    }


@app.route('/api/topic-model', methods=['POST'])
def topic_modelling():
    data = request.get_json()
    tme = TopicModellingEntity(data['topics'], data['text'])
    input_to_llm = 'Extract various parts of the given text into items like {}, text: {}'.format(tme.topics, tme.text)
    print(input_to_llm)
    return {
        'topicModellingOutput': parts_of_speech(input_to_llm)
    }, 200


@app.route('/api/sentiment-score', methods=['POST'])
def sentiment_scoring():
    data = request.get_json()
    sae = SentimentAnalysisEntity(data['text'])
    print(sae.text)
    return {
        'sentimentScore': sentiment_analysis(sae.text)
    }, 200


def parts_of_speech(tm_input):
    vertexai.init(
        project="ac-cntxtlbank-sct-project",
        location="us-central1",
    )
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained("text-bison@001")

    response = model.predict(
        tm_input,
        **parameters
    )
    print(f"Response from Model: \n")
    print(response.text)
    return response.text


def sentiment_analysis(input_to_transformer):
    classifier = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")
    result = classifier(input_to_transformer)
    print(result)  # [{'label': 'POSITIVE', 'score': 0.9989916682243347}]
    return {
        'inputText': input_to_transformer,
        'sentimentScore': result
    }


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("starting server at [127.0.0.1:5000] ... ")
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
