import json

import vertexai
from transformers import pipeline
from vertexai.language_models import TextGenerationModel

vertexai.init(
    project="hack-team-neuralsquad",
    location="us-central1",
)
parameters = {
    "temperature": 0.2,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40
}
vertex_palm_model = TextGenerationModel.from_pretrained("text-bison@001")
bert_text_sentiment_model = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")


def parts_of_speech_vertex(tm_input):

    print('calling VertexAi for predictions...')
    response = vertex_palm_model.predict(
        tm_input,
        **parameters
    )
    print(f"Response from Model: \n")
    print(response.text)
    return response.text


def sentiment_analysis_bert(input_to_transformer):
    result = bert_text_sentiment_model(input_to_transformer)
    print(result)  # [{'label': 'POSITIVE', 'score': 0.9989916682243347}]
    return {
        'inputText': input_to_transformer,
        'sentimentScore': result
    }


def email_classification_vertex(email_text):
    result = vertex_palm_model.predict(
        email_text,
        **parameters
    )
    print(result)
    return {
        'inputText': email_text,
        'emailClassificationResult': {
            'response': json.loads(result.text),
            'safety_attributes': result.safety_attributes
        }
    }
