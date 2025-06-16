from google import genai
from google.genai import types

def generate():
  client = genai.Client(
      vertexai=True,
      project="hy-20250609-001",
      location="global",
  )

  # Note: Part.from_uri typically expects a Google Cloud Storage URI (gs://...).
  # Support for YouTube URLs may vary.
  video1 = types.Part.from_uri(
      file_uri="https://www.youtube.com/watch?v=TOuF7ZbcCUs",
      mime_type="video/*",
  )

  video_metadata = types.VideoMetadata(
    fps=0.1
  )

  # Using a standard and recent model name.
  model = "gemini-1.5-flash-latest"
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

  # Removed media_resolution as it was incomplete and is an optional parameter.
  generate_content_config = types.GenerateContentConfig(
    temperature = 1,
    top_p = 1,
    seed = 0,
    )
  

  for chunk in client.models.generate_content_stream(
    model = model,
    contents = contents,
    config = generate_content_config,
    ):
    print(chunk.text, end="")

generate()
