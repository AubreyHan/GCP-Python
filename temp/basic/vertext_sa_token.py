from google.oauth2 import service_account
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting, FinishReason
import vertexai.preview.generative_models as generative_models

cred = service_account.Credentials.from_service_account_file(
    '/home/gcpvm/sakey/hy-ai-demo.json')

def generate():
    vertexai.init(project="hy-ai-demo", location="us-central1", credentials=cred)
    model = GenerativeModel(
        "gemini-1.5-flash-001",
    )
    responses = model.generate_content(
      ["""请描述一个小动物"""],
      generation_config=generation_config,
      safety_settings=safety_settings,
      stream=True,
    )

    for response in responses:
        print(response.text, end="")


generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH
    ),
]

generate()