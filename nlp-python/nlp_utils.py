import vertexai
from transformers import pipeline
from vertexai.language_models import TextGenerationModel

import os


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.expanduser(
    '~/.config/gcloud/application_default_credentials.json')


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

    print('calling VertexAi for predictions...')
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
