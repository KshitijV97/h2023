# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import vertexai
from vertexai.language_models import TextGenerationModel

def parts_of_speech():

    vertexai.init(project="ac-cntxtlbank-sct-project", location="us-central1", credentials="ya29.a0AWY7Ckl6UMaP9Zn94otPrQ10ZIpdeV8C5MVyDS5NBJyk08tglL-fPR_33yxw9yGQ3tflPKTAhPf4q8j8HHNvMR5IssqvR8IndWs8UCMLiGWmJwOfOAvH10DBqzL0O7AgWAY82QGIKMoj-C4XPrQWoQBK_wU3mzr7TObODpcaCgYKAS0SARISFQG1tDrpPKiP9mBcPE2LZwXOM_ZKhA0174")
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(
        """Extract various parts of the given text into items like email, address, phone number. 
    text: Hi, My name is Yash Patil, i work with Google Cloud Platform and live in Privet Drive, Surrey. You can contact me at 9876543210
    """,
        **parameters
    )
    print(f"Response from Model: {response.text}")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    parts_of_speech()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
