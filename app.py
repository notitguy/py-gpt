import os
from dotenv import load_dotenv
load_dotenv()

ENV_GPT = os.getenv('OPENAI_API_KEY')

from openai import OpenAI

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

def BasicGeneration(userPrompt):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": userPrompt}
    ]
  )
  return completion.choices[0].message.content

promt = "explain programming in two words"
response =BasicGeneration(promt)
print(response)