from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-6-luna",
    input="Who FIFA world cup in 2026 and what is the final score. Give short answer"
)

print(response.output_text)
