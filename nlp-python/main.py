# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import vertexai
from vertexai.language_models import TextGenerationModel
from transformers import pipeline

import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.expanduser(
    '~/.config/gcloud/application_default_credentials.json')


def parts_of_speech(input_to_llm):
    vertexai.init(
        project="ac-cntxtlbank-sct-project",
        location="us-central1",
        # credentials=credentials
    )
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained("text-bison@001")

    response = model.predict(
        input_to_llm,
        **parameters
    )
    print(f"Response from Model: \n")
    print(response.text)


def sentiment_analysis(input_to_transformer):
    classifier = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")
    result = classifier(input_to_transformer)
    print(result)   #[{'label': 'POSITIVE', 'score': 0.9989916682243347}]
    print(result[0]['score'])

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_to_llm = """Extract various parts of the given text into items like email, address, phone number. 
        text: Hi, My name is Yash Patil, i work with Google Cloud Platform and live in Privet Drive, Surrey. 
        You can contact me at 9876543210
        """
    input_for_sentiment = """Give me the sentiment analysis (both score and magnitude) of the below text. 
        text: For the third year running, Deutsche Bank’s Foreign Exchange (FX) 
        business has scooped Best Liquidity Provider for Forwards/Swaps and placed top 
        in a new category - Best New Algo - in FX Markets’ eFX Awards 2023.
        """
    # parts_of_speech(input_to_llm)
    sentiment_analysis(input_for_sentiment)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
