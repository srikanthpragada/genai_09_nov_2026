# Create key using https://aistudio.google.com/apikey
# Set environment variable GOOGLE_API_KEY to Gemini API key

# Using google Interactions API

from google import genai

client = genai.Client()

response = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input="What is the capital of Spain?"
)

#print(response)
print(response.output_text)