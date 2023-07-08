# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request

from models import SentimentAnalysisEntity, TopicModellingEntity
from nlp_utils import parts_of_speech, sentiment_analysis

app = Flask(__name__)


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


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("starting server at [127.0.0.1:5000] ... ")
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
