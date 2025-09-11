from google import genai
from google.genai import types
import base64
import os

def generate():
  client = genai.Client(
      vertexai=True,
      api_key=os.environ.get("GOOGLE_CLOUD_API_KEY"),
  )

  msg2_text1 = types.Part.from_text(text="""**Returning a Greeting**

I've processed your simple greeting and noted the lack of specific data for the schema. My current thought is to return a reciprocal greeting as a basic, albeit optional, response.

**Generating a Response**

I've analyzed your simple greeting and the constraints of the schema. My current thinking is to provide a reciprocal greeting in the optional \"response\" field, as there's no other specific data to process.""")

  model = "gemini-2.5-flash"
  contents = [
    types.Content(
      role="user",
      parts=[
        types.Part.from_text(text="""hello""")
      ]
    ),
    types.Content(
      role="model",
      parts=[
        msg2_text1,
        types.Part.from_text(text="""{
  \"response\": \"Hello there!\"
}""")
      ]
    ),
    types.Content(
      role="user",
      parts=[
        types.Part.from_text(text="""hello""")
      ]
    ),
  ]

  generate_content_config = types.GenerateContentConfig(
    temperature = 1,
    top_p = 1,
    max_output_tokens = 65535,
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="OFF"
    )],
    response_mime_type = "application/json",
    response_schema = {"type":"OBJECT","properties":{"response":{"type":"STRING"}}},
    thinking_config=types.ThinkingConfig(
      thinking_budget=-1,
    ),
  )

  for chunk in client.models.generate_content_stream(
    model = model,
    contents = contents,
    config = generate_content_config,
    ):
    print(chunk.text, end="")

generate()


