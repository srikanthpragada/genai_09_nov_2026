# Set environment variable GROQ_API_KEY

from langchain_groq import ChatGroq

# Initialize Groq LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b"
)

response = llm.invoke("Which is the capital of India")
print(response.content)