from google import genai
from google.genai import types
from google.genai.types import (
    FunctionDeclaration,
    GenerateContentConfig,
    Tool,
)

client = genai.Client(vertexai=True, location="us-central1", project='ai-demo-440003')
model_id = "gemini-2.0-flash-001"

#创建FunctionDeclaration
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

contents = [
    types.Content(
        role="user", parts=[types.Part(text="what is the sum of 2 and 3?")]
    )
]

config=GenerateContentConfig(
        tools=[sum_tool],
        temperature=0
        )

response = client.models.generate_content(
    model=model_id,
    contents=contents,
    config=config,
    )

print(response.candidates[0].content.parts[0].function_call.args)
tool_call = response.candidates[0].content.parts[0].function_call
result = get_sum(**tool_call.args)

function_response_part = types.Part.from_function_response(
    name=tool_call.name,
    response={'response': result}
)

contents.append(types.Content(role="model", parts=[types.Part(function_call=tool_call)]))
contents.append(types.Content(role="user", parts=[function_response_part]))

final_response = client.models.generate_content(
    model="gemini-2.0-flash",
    config=GenerateContentConfig(
        tools=[sum_tool],
        temperature=0
        ),
    contents=contents,
)

print(final_response.text)