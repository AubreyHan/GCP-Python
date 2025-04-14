from google import genai
from google.genai import types

client = genai.Client(vertexai=True, location="us-central1", project='ai-demo-440003')

prompt = 'explain the difference between a and b'
model = 'gemini-2.0-flash-thinking-exp-01-21'

config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_budget=0),
)

response = client.models.generate_content(
    model=model,
    contents=prompt
)

print(response)