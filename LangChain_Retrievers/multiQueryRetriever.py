from langchain_community.vectorstores import FAISS
from langchain_huggingface import (
    HuggingFaceEndpointEmbeddings, 
    ChatHuggingFace, 
    HuggingFaceEndpoint
)
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_core.documents import Document

from dotenv import load_dotenv

load_dotenv()

# Relevant health & wellness documents
all_docs = [
    Document(
        page_content="Regular walking boosts heart health and can reduce symptoms of depression.",
        metadata={"source": "H1"}
    ),
    Document(
        page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.",
        metadata={"source": "H2"}
    ),
    Document(
        page_content="Deep sleep is crucial for cellular repair and emotional regulation.",
        metadata={"source": "H3"}
    ),
    Document(
        page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.",
        metadata={"source": "H4"}
    ),
    Document(
        page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.",
        metadata={"source": "H5"}
    ),
    Document(
        page_content="The solar energy system in modern homes helps balance electricity demand.",
        metadata={"source": "I1"}
    ),
    Document(
        page_content="Python balances readability with power, making it a popular system design language.",
        metadata={"source": "I2"}
    ),
    Document(
        page_content="Photosynthesis enables plants to produce energy by converting sunlight.",
        metadata={"source": "I3"}
    ),
    Document(
        page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.",
        metadata={"source": "I4"}
    ),
    Document(
        page_content="Black holes bend spacetime and store immense gravitational energy.",
        metadata={"source": "I5"}
    ),
]

# LLM
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-4-31B-it",
    task="conversational"
)

chat_model = ChatHuggingFace(llm = llm)

# Embedding model
embedding = HuggingFaceEndpointEmbeddings(
    model = "sentence-transformers/all-MiniLM-L6-v2",
)

# Create FAISS vector store
vectorStore = FAISS.from_documents(
    documents=all_docs, 
    embedding=embedding
)

# Create similarity retrievers
similarity_retriever = vectorStore.as_retriever(
    search_type='similarity',
    search_kwargs={'k':5}
)

# Create MultiQuery retrievers
multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vectorStore.as_retriever(
        search_kwargs={'k':5}
    ),
    llm=chat_model
)

# Query
query = 'How to improve energy levels and maintain balance?'

# Retrieve results
similarity_results = similarity_retriever.invoke(query)
multiquery_results = multiquery_retriever.invoke(query)


# Similarity results
print("\n" + "=" * 60)
print("SIMILARITY RETRIEVER RESULTS")
print("=" * 60)

for i, doc in enumerate(similarity_results):
    print(f"\n--- Result {i + 1} ---")
    print(f"Content: {doc.page_content}")
    print(f"Metadata: {doc.metadata}")


# MultiQuery results
print("\n" + "=" * 60)
print("MULTI-QUERY RETRIEVER RESULTS")
print("=" * 60)

for i, doc in enumerate(multiquery_results):
    print(f"\n--- Result {i + 1} ---")
    print(f"Content: {doc.page_content}")
    print(f"Metadata: {doc.metadata}")