import sys 
import json
import os
from openai import OpenAI

OPENAI_TOKEN = os.getenv("OPENAI_TOKEN", "no-token")
PROMPT = os.getenv("PROMPT", "no-prompt")

client = OpenAI(
    api_key=OPENAI_TOKEN,
)


raw_data = sys.stdin.read()
data = json.loads(raw_data)
commits = data["commits"]


prompt = f"""{PROMPT} 
Commits:
{commits}
"""

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-4o-mini",
)
output = chat_completion.choices[0].message.content

print(f"::set-output name=num_squared::{output}")
