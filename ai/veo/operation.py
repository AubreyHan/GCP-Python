from google import genai
from google.genai import types
from google.genai.errors import ClientError
import time

client = genai.Client(
    vertexai=True,
    project="ai-demo-440003",
    location="us-central1",
)

operation = client.models.generate_videos(
    model="veo-3.0-generate-preview",
    prompt="A cinematic shot of a majestic lion in the savannah.",
)

print(f"Operation started: {operation.name}")
# Alternatively, you can use the operation.name to get the operation
operation = types.GenerateVideosOperation(name=operation.name)

# This loop checks the job status every 10 seconds
while not operation.done:
    print(operation)
    time.sleep(10)
    # Refresh the operation object to get the latest status
    operation = client.operations.get(operation)