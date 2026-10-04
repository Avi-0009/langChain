from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

# Source document
documents = [
    Document(page_content='Langchain helps developers build LLM application easily.'),
    Document(page_content='Chroma is a vector database optimized for LLM-based search.'),
    Document(page_content='Embeddings convert text into the high-dimensional vectors.'),
    Document(page_content='OpenAI provides powerful embedding models.')
]

# Initialize embedding model
model = OpenAIEmbeddings()

# Create Chroma vector store in memory
vectorStore = Chroma.from_documents(
    documents=documents,
    embedding=model,
    collection_name='my_collection'
)

# Convert vectorStore into a retriever
retriever = vectorStore.as_retriever(search_kwargs={'k':2})

query = 'What is Chroma used for?'
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f'\n --- Result {i+1} ---')
    print(f'Content:\n {doc.page_content}...')