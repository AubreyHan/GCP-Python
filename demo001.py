from google import genai
from google.genai import types
import base64

def generate():
  client = genai.Client(
      vertexai=True,
      project="hy-ai-demo",
      location="us-central1",
  )


  model = "gemini-2.5-pro-preview-03-25"
  contents = [
    types.Content(
      role="user",
      parts=[
        types.Part.from_text(text='请描述广义相对论?')
      ]
    )
  ]
  generate_content_config = types.GenerateContentConfig(
    temperature = 1,
    top_p = 0.95,
    max_output_tokens = 8192,
    response_modalities = ["TEXT"],
    speech_config = types.SpeechConfig(
      voice_config = types.VoiceConfig(
        prebuilt_voice_config = types.PrebuiltVoiceConfig(
          voice_name = "zephyr"
        )
      ),
    ),
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

  print(response)

#   for chunk in client.models.generate_content(
#     model = model,
#     contents = contents,
#     config = generate_content_config,
#     ):
#     print(chunk.text, end="")



generate()