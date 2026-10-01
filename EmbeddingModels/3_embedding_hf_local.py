from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEndpointEmbeddings(
    model = "sentence-transformers/all-MiniLM-L6-v2",
)

# text = "Delhi is the capital of India."
documents = [
    "Delhi is the capital of India",
    "Lucknow is the capital of Uttar Pradesh",
    "Paris is the capital of France"
]

vector = embedding.embed_documents(documents)

print(str(vector))