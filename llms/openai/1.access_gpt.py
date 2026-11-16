# Create key using https://platform.openai.com/api-keys
# Set environment variable OPENAI_API_KEY to OpenAI key.
# https://developers.openai.com/api/docs

from openai import OpenAI

client = OpenAI()
#client = OpenAI(api_key="dfsadfadsfsdafsd")

response = client.responses.create(
    model="gpt-6-luna",
    input="What is the capital of Spain?"
)

#print(response)
print(response.output_text)
