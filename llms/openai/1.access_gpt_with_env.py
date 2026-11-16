# Create key using https://platform.openai.com/api-keys
# Place variable OPENAI_API_KEY in .env file

from dotenv import load_dotenv
# Load variables from .env into the system memory
load_dotenv(override=True)

import os 
api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-6-luna",
    input="What is the capital of Spain?"
)

#print(response)
print(response.output_text)
