# Set environment variable GOOGLE_API_KEY to Google key.

from langchain.chat_models import init_chat_model
from google.genai.types import AutomaticFunctionCallingConfig
from langchain_core.prompts import PromptTemplate

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

# To supress warning from google SDK
model = model.bind(automatic_function_calling=AutomaticFunctionCallingConfig(disable=True))


template_str = """Write a {lang} function for the following requirement:
{text}

Give the most efficient and simple to understand code. Do not give any test code and explanation. 
"""
prompt_template = PromptTemplate.from_template(template=template_str)
prompt = prompt_template.format(
    lang="java",
    text="Check whether a number is perfect number or not")


response = model.invoke(prompt)
print(response.content)
