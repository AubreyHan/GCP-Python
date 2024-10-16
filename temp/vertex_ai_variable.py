import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting
from vertexai.preview.prompts import Prompt
from google.oauth2 import service_account

cred = service_account.Credentials.from_service_account_file(
    '/home/gcpvm/sakey/hy-ai-demo.json')

def generate():
    vertexai.init(project="hy-ai-demo", location="us-central1",credentials=cred)
    model = GenerativeModel(
        "gemini-1.5-pro-002",
    )
    responses = model.generate_content(
        ["""请总结如下video""", video1],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    for response in responses:
        print(response.text, end="")
    
    print(responses)

video1 = Part.from_uri(
    mime_type="video/mp4",
    uri="gs://hy-ai-bucket/06.mp4",
)

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
]

generate()