from google import genai
from google.genai import types

client = genai.Client(vertexai=True, location="us-central1", project='ai-demo-440003')

config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
        thinking_budget=100,    #控制Thinking的token数(1-24576，1024以下会统一为1024，0表示关闭)
        include_thoughts=True,  #输出是否包含思考过程的汇总
    ), 
)

response = client.models.generate_content(
    model="gemini-2.5-flash-preview-04-17",
    contents='''Hello there! How can I help you today?''',
    #config=config
)

print(response.text)
print('input_token:',response.usage_metadata.prompt_token_count) 
print('thought_token:',response.usage_metadata.thoughts_token_count)
print('output_token:',response.usage_metadata.candidates_token_count)
print('total_token:',response.usage_metadata.total_token_count)



