from google import genai
from google.genai import types
from google.genai.errors import ClientError

def generate():
  client = genai.Client(
      vertexai=True,
      project="hy-20250701-001",
      location="us-central1",
  )


  model = "gemini-2.5-flash"
  contents = [
    types.Content(
      role="user",
      parts=[
        types.Part.from_text(text="""hello""")
      ]
    ),
  ]
  generate_content_config = types.GenerateContentConfig(
    temperature = 0.2,
    top_p = 0.8,
    max_output_tokens = 1024,
    response_modalities = ["TEXT"],
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

  response = client.models.generate_content(
    model=model,
    contents=contents,
    config=generate_content_config,
  )

  print(response.text)

while True:
  try:
    generate()
  except ClientError as e:
    if e.code == 429:
      continue


