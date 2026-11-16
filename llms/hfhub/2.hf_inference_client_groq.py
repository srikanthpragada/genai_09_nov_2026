## Set environment variable - HF_TOKEN - to access token 

from huggingface_hub import InferenceClient
import keys 

client = InferenceClient(provider="groq",
                         api_key=keys.GROQ_API_KEY,
                         model="openai/gpt-oss-120b")

messages = [
    {"role": "user", "content": "What is the capital of France?"}
]
response = client.chat_completion(messages)
#print(response)
print(response.choices[0].message.content)
