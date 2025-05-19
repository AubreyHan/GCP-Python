import asyncio
import os
from datetime import datetime
from google import genai
from google.genai import types
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

client = genai.Client(
    vertexai=True,
    project='ai-demo-440003',
    location='us-central1',
)

server_params = StdioServerParameters(
    command='npx',
    args=['-y', 'phischmid/weather-macp'],
    env=None,
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            prompt = f"What is the weather in London in {datetime.now().strftime('%Y-%m-%d')}?"
            await session.initialize()

            mcp_tools = await session.list_tools()
            print(f"Available tools: {mcp_tools}")

asyncio.run(run())