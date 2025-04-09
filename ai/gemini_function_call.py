from google import genai
from google.genai.types import (
    FunctionDeclaration,
    GenerateContentConfig,
    HttpOptions,
    Tool,
)

client = genai.Client(vertexai=True, location="us-central1", project='ai-demo-440003')
model_id = "gemini-2.0-flash-001"

get_sum = FunctionDeclaration(
    name="get_sum",
    description="Calculate the sum of two numbers.",
    parameters={
        "type": "object",
        "properties": {
            'a': {"type": "number", "description": "The first number."},
            'b': {"type": "number", "description": "The second number."},
        },
        "required": ['a', 'b'],
    },
)

sum_tool = Tool(function_declarations=[get_sum])

def get_sum(a: float, b: float) -> float:
    """Calculate the sum of two numbers."""
    return a + b    

response = client.models.generate_content(
    model=model_id,
    contents='calculate the sum of 1 and 2',
    config=GenerateContentConfig(
        tools=[sum_tool],
        temperature=0
        ),
    )

print(response.candidates[0].content.parts[0].function_call.args)
tool_call = response.candidates[0].content.parts[0].function_call
print(get_sum(**tool_call.args))
