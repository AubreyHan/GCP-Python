import time
from google import genai
from google.genai.types import GenerateVideosConfig

client = genai.Client(vertexai=True, project='ai-demo-440003', location='us-central1')

# TODO(developer): Update and un-comment below line
# output_gcs_uri = "gs://your-bucket/your-prefix"

operation = client.models.generate_videos(
    model="veo-3.0-fast-generate-preview",
    prompt="a cat reading a book",
    config=GenerateVideosConfig(
        aspect_ratio="16:9",
        output_gcs_uri='gs://hy-aibucket-001',
    ),
)

while not operation.done:
    time.sleep(15)
    operation = client.operations.get(operation)
    print(operation)

if operation.response:
    print(operation.result.generated_videos[0].video.uri)

# Example response:
# gs://your-bucket/your-prefix