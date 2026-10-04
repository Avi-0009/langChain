# Maximum Marginal Relevance 
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

# Initializing HuggingFace embedding
model = HuggingFaceEndpointEmbeddings(
    model = "sentence-transformers/all-MiniLM-L6-v2",
)

docs = [
    Document(page_content='LangChain makes it easy to work with LLMs.'),
    Document(page_content='LangChain is used to build LLM based application.'),
    Document(page_content='Chroma is used to store and search document embeddings.'),
    Document(page_content='Embeddings are vector representations of text.'),
    Document(page_content='MMR helps you get diverse results when doing similarity search.'),
    Document(page_content='LangChain supports Chroma, FAISS, Pinecode and more.')
]

# Create the FAISS vector store from documents
vectorStore = FAISS.from_documents(
    documents=docs,
    embedding=model
)

# Enable MMR in the retriever
retriever = vectorStore.as_retriever(
    search_type='mmr',
    search_kwargs={'k':3, 'lambda_mult':0.3} # k top results, lambda_mult = relevance diversity balance (0 to 1, the lesser the value the better the response)
)

query = 'what is langchain?'
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f'\n --- Result {i+1} ---')
    print(f'Content:\n {doc.page_content}...')