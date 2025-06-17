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

  model = "gemini-2.0-flash-001"
  contents = [
    types.Content(
      role="user",
      parts=[
        video1,
        video_metadata,
        types.Part.from_text(text="""请说明gemini在分析此视频时的采样率""")
      ]
    )
  ]

  generate_content_config = types.GenerateContentConfig(
    temperature = 1,
    top_p = 1,
    seed = 0,
    media_resolution = types.MediaResolution.MEDIA_RESOLUTION_LOW
    )
  

  for chunk in client.models.generate_content_stream(
    model = model,
    contents = contents,
    config = generate_content_config,
    ):
    print(chunk.text, end="")

generate()
print("Hello, world")