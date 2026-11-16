# Set environment variable - HUGGINGFACE_HUB_TOKEN - to access token
 
from langchain.chat_models import init_chat_model
model =  init_chat_model("groq:openai/gpt-oss-120b", temperature=0)

response = model.invoke("Which is the capital of Sweden?")
print(response.content)
