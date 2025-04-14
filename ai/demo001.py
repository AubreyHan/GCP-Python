from google import genai
from google.genai import types
from google.genai.errors import ClientError

try:
    
except ClientError as e:
    print(f"An error occurred: {e}")