# Set environment variable GOOGLE_API_KEY to Google key.

from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-3.5-flash-lite", model_provider="google_genai")

#response = model.invoke("Who is James Gosling")
response = model.stream("Who is Van Rossum?")

for chunk in response:
    print(chunk.content, end = "\n--------------\n")
