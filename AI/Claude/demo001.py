# TODO(developer): Vertex AI SDK - uncomment below & run
# pip3 install --upgrade --user google-cloud-aiplatform
# gcloud auth application-default login
# pip3 install -U 'anthropic[vertex]'

# TODO(developer): Update and un-comment below line
# PROJECT_ID = "your-project-id"

from anthropic import AnthropicVertex

client = AnthropicVertex(project_id='hy-ai-demo', region="us-east5")
result = []

with client.messages.stream(
    model="claude-sonnet-4@20250514",
    max_tokens=3024,
    messages=[
        {
            "role": "user",
            "content": "hello.",
        }
    ],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
        result.append(text)

# Example response:
# Here's a simple recipe for delicious banana bread:
# Ingredients:
# - 2-3 ripe bananas, mashed
# - 1/3 cup melted butter
# ...
# ...
# 8. Bake for 50-60 minutes, or until a toothpick inserted into the center comes out clean.
# 9. Let cool in the pan for a few minutes, then remove and cool completely on a wire rack.