from google import genai
from google.genai import types
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/yuanhancn/Tools/python/SAKey/hy-ai-demo.json'

def generate():
  client = genai.Client(
      vertexai=True,
      project='hy-ai-demo',
      location='global',
      http_options=types.HttpOptions(timeout=20000)
  )


  model = "gemini-2.5-flash-image-preview"
  contents = [
    types.Content(
      role="user",
      parts=[
        types.Part.from_text(text="""请画一只小狗""")
      ]
    )
  ]

  generate_content_config = types.GenerateContentConfig(
    temperature = 1,
    top_p = 0.95,
    max_output_tokens = 32768,
    response_modalities = ["TEXT", "IMAGE"],
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
  )

  for chunk in client.models.generate_content_stream(
    model = model,
    contents = contents,
    config = generate_content_config,
    ):
    print(chunk.text, end="")

generate()