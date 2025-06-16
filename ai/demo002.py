from google import genai
from google.genai import types

def generate():
  client = genai.Client(
      vertexai=True,
      project="hy-20250609-001",
      location="global",
  )

  video1 = types.Part.from_uri(
      file_uri="https://www.youtube.com/watch?v=TOuF7ZbcCUs",
      mime_type="video/*",
  )

  video_metadata = types.VideoMetadata(
    fps=0.1
  )

  model = "gemini-2.5-pro-preview-06-05"
  contents = [
    types.Content(
      role="user",
      parts=[
        video1,
        video_metadata,
        types.Part.from_text(text="""请详细描述以上视频""")
      ]
    )
  ]

  generate_content_config = types.GenerateContentConfig(
    temperature = 1,
    top_p = 1,
    seed = 0,
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