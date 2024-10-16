import vertexai
from google.oauth2 import service_account

cred = service_account.Credentials.from_service_account_file(
    '/home/gcpvm/sakey/hy-ai-demo.json')

from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
    Tool,
    grounding,
)

# TODO(developer): Update and un-comment below line
project_id = "hy-ai-demo"

vertexai.init(project=project_id, location="us-central1", credentials=cred)

model = GenerativeModel("gemini-1.5-flash-001")

# Use Google Search for grounding
tool = Tool.from_google_search_retrieval(grounding.GoogleSearchRetrieval())

prompt = "When is the next total solar eclipse in US?"
response = model.generate_content(
    prompt,
    tools=[tool],
    generation_config=GenerationConfig(
        temperature=0.0,
    ),
)

print(response)