# Create key using https://platform.openai.com/api-keys
# Set environment variable OPENAI_API_KEY to OpenAI key.
# https://developers.openai.com/api/docs

from dotenv import load_dotenv
# Load variables from .env into the system memory
load_dotenv(override=True)

import os 
api_key = os.getenv("OPENAI_API_KEY")
print(api_key)


from openai import OpenAI


client = OpenAI()
#client = OpenAI(api_key="dfsadfadsfsdafsd")

response = client.responses.create(
    model="gpt-6-luna",
    input="What is the capital of Spain?"
)

#print(response)
print(response.output_text)
