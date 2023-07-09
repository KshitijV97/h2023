import vertexai
from transformers import pipeline
from vertexai.language_models import TextGenerationModel

import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.expanduser(
    '~/.config/gcloud/application_default_credentials.json')


def init_vertex():
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
    return model, parameters


def parts_of_speech_vertex(tm_input):

    model, parameters = init_vertex()

    print('calling VertexAi for predictions...')
    response = model.predict(
        tm_input,
        **parameters
    )
    print(f"Response from Model: \n")
    print(response.text)
    return response.text


def sentiment_analysis_bert(input_to_transformer):
    classifier = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")
    result = classifier(input_to_transformer)
    print(result)  # [{'label': 'POSITIVE', 'score': 0.9989916682243347}]
    return {
        'inputText': input_to_transformer,
        'sentimentScore': result.text
    }


def email_classification_vertex(email_text):
    model, parameters = init_vertex()
    result = model.predict(
        email_text,
        **parameters
    )
    print(result)
    return {
        'inputText': email_text,
        'emailClassificationResult': {
            'response': result.text,
            'safety_attributes': result.safety_attributes
        }
    }
