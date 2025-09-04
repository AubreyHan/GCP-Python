from google import genai

client = genai.Client(
    project='hy-ai-demo',
    vertexai=True,
    location="global"
)

prompt = (
    "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"
)

response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[prompt],
)