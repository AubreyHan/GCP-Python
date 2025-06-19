from google import genai
from google.genai import types
from google.auth import default

client = genai.Client(
    vertexai=True,  project='ai-demo-440003', location='us-central1'
)

video_file_name = "/Users/yuanhancn/Tools/FFMpeg/20min.mp4"
video_bytes = open(video_file_name, 'rb').read()


response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=types.Content(
        role='user',
        parts=[
            types.Part(
                inline_data=types.Blob(
                    data=video_bytes,
                    mime_type='video/mp4'),
                video_metadata=types.VideoMetadata(fps=1)
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)

print(response)