from google import genai
from google.genai import types

client = genai.Client(vertexai=True, location="us-central1", project='ai-demo-440003')
model_id = "gemini-2.0-flash-001"

def get_sum_function(a: float, b: float) -> float:
    """Calculate the sum of two numbers."""
    return a + b

config = types.GenerateContentConfig(
    tools=[get_sum_function]
)

contents = [
    types.Content(
        role="user", parts=[types.Part(text="what is the sum of 2 and 3?")]
    )
]

response = client.models.generate_content(
    model=model_id,
    contents=contents,
    config=config,
)

print(response.text)