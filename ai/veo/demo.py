from google import genai
from google.genai import types

client = genai.Client(
    vertexai=True,
    project="ai-demo-440003",
    location="us-central1",
)

operation_name = 'projects/ai-demo-440003/locations/us-central1/publishers/google/models/veo-3.0-generate-preview/operations/83451d58-f795-46fb-8e8b-85d096b8a274'

operation = types.GenerateVideosOperation(name=operation_name)
operation = client.operations.get(operation)

print(operation.done)