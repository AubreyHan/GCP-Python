import os
from google.auth import default
import google.auth.transport.requests
import openai
import random

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/yuanhancn/Tools/GithubRepo/GCP-SA/hy-20250609-001-6ba55150037b.json'

credentials, _ = default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
credentials.refresh(google.auth.transport.requests.Request())

project_id = 'hy-20250609-001'
location = 'us-central1'
model = 'google/gemini-2.0-flash-001'
ENDPOINT_ID = 'openapi'

client = openai.OpenAI(
    base_url=f"https://{location}-aiplatform.googleapis.com/v1/projects/{project_id}/locations/{location}/endpoints/{ENDPOINT_ID}",
    api_key=credentials.token
)

response = client.chat.completions.create(
       model=model,
       messages=[
           {'role': "user",
            'content': [
                {'type': 'text',
                 'text': 'What is in this image?',                    
                },
                {'type': 'image_url',
                 'image_url': {'url': 'gs://hy-gemini-gcs/1.jpg'}
                }
            ]
            }
       ],
   )

print(response)
