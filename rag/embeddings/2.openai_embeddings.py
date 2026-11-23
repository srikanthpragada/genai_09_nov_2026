from langchain_openai import OpenAIEmbeddings

embeddings_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

docs = [
    "Liverpool is winning a lot of matches",
    "Ollama allows running LLMs locally.",
    "Manchester City is doing awesome!",
    "Bill Gates Founded Microsoft",
    "Real Madrid won UEFA Champions League 13 times."
 ]

embeddings = embeddings_model.embed_documents(docs)
print(len(embeddings), len(embeddings[0]))
print(embeddings[0][:10])
