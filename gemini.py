from google import genai
from google.genai import types
from helpers import get_prompt

client = genai.Client()

prompt = ""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=get_prompt(job_url),
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0)
    ),
)

print(response.text)