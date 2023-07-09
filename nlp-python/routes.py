from flask import Blueprint, request

from models import TopicModellingEntity, SentimentAnalysisEntity, EmailClassificationEntity
from nlp_utils import parts_of_speech_vertex, sentiment_analysis_bert, email_classification_vertex

# Create a blueprint instance
routes_blueprint = Blueprint('routes', __name__)

# Define your routes and corresponding functions
@routes_blueprint.route('/health')
def health():
    return {
        "status": "UP"
    }

@routes_blueprint.route('/api/topic-model', methods=['POST'])
def topic_modelling():
    data = request.get_json()
    tme = TopicModellingEntity(data['topics'], data['text'])
    input_to_llm = 'Extract various parts of the given text into items like {}, text: {}'.format(tme.topics, tme.text)
    print(input_to_llm)
    return {
        'topicModellingOutput': parts_of_speech_vertex(input_to_llm)
    }, 200


@routes_blueprint.route('/api/sentiment-score', methods=['POST'])
def sentiment_scoring():
    data = request.get_json()
    sae = SentimentAnalysisEntity(data['text'])
    return {
        'sentimentScore': sentiment_analysis_bert(sae.text)
    }, 200


@routes_blueprint.route('/api/email-classification', methods=['POST'])
def email_classification():
    data = request.get_json()
    ece = EmailClassificationEntity(data['subject'], data['body'])
    input_to_email_classifier = 'extract below email text into banking enquiry categories like ' \
                                'loan application enquiry, credit card enquiry, account statement request and more, ' \
                                'text: {}'.format(ece.body)
    return {
        'emailClassificationResults': email_classification_vertex(input_to_email_classifier)
    }, 200
