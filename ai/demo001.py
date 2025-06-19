video_file_name = "/Users/yuanhancn/Tools/FFMpeg/5noaudio.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = 

response = client.models.generate_content(
    model='models/gemini-2.5-flash-preview-05-20',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(
                    data=video_bytes,
                    mime_type='video/mp4'),
                video_metadata=types.VideoMetadata(fps=5)
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)

print(response)