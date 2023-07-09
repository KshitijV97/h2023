from flask import Blueprint, request

from models import TopicModellingEntity, SentimentAnalysisEntity
from nlp_utils import parts_of_speech, sentiment_analysis

# Create a blueprint instance
routes_blueprint = Blueprint('routes', __name__)

# Define your routes and corresponding functions
@routes_blueprint.route('/health')
def health():
    return {
        "status": "UP"
    }

@routes_blueprint.route('/api/data')
def get_data():
    return 'Data endpoint'


@routes_blueprint.route('/api/topic-model', methods=['POST'])
def topic_modelling():
    data = request.get_json()
    tme = TopicModellingEntity(data['topics'], data['text'])
    input_to_llm = 'Extract various parts of the given text into items like {}, text: {}'.format(tme.topics, tme.text)
    print(input_to_llm)
    return {
        'topicModellingOutput': parts_of_speech(input_to_llm)
    }, 200


@routes_blueprint.route('/api/sentiment-score', methods=['POST'])
def sentiment_scoring():
    data = request.get_json()
    sae = SentimentAnalysisEntity(data['text'])
    print(sae.text)
    return {
        'sentimentScore': sentiment_analysis(sae.text)
    }, 200
