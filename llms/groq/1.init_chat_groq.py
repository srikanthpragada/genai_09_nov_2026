 
from langchain.chat_models import init_chat_model
model =  init_chat_model("openai/gpt-oss-20b")

response = model.invoke("Which is the capital of Sweden?")
print(response.content)
