from google import genai
from google.genai import types

client = genai.Client(vertexai=True, location="us-central1", project='ai-demo-440003')

config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_budget=0), 
)

response = client.models.generate_content(
    model="gemini-2.5-flash-preview-04-17",
    contents='''How many R's are in the word strawberry?''',
    config=config
)

print(response.usage_metadata.thoughts_token_count)

