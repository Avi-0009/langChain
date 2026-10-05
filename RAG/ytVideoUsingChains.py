from langchain_huggingface import (
    HuggingFaceEndpointEmbeddings, 
    HuggingFaceEndpoint,
    ChatHuggingFace
)

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableParallel,
    RunnableLambda
)
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable
)

from dotenv import load_dotenv

load_dotenv()

## Indexing

# Document Ingestion

video_id = "Gfr50f6ZBvo"
transcript_text = ""

try:
    ytt_api = YouTubeTranscriptApi()

    transcript = ytt_api.fetch(
        video_id=video_id,
        languages=['en']
    )

    transcript_text = " ".join(
        snippet.text for snippet in transcript
    )

except TranscriptsDisabled:
    print("No captions available for this video.")

except NoTranscriptFound:
    print("No English transcript found for this video.")

except VideoUnavailable:
    print("The video is unavailable.")

except Exception as e:
    print(f"Something went wrong: {e}")


# Text Splitting

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 200
)

chunks = splitter.create_documents([transcript_text])


# Hugging Face Embeddings

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction"
)


# FAISS vector store

vectorStore = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings
)


# Retriever

retriever = vectorStore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)


# HUGGING FACE LLM

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-4-31B-it",
    task="conversational",
    temperature=0.2,
    max_new_tokens=512
)

chat_model = ChatHuggingFace(
    llm=llm
)


# Prompt

prompt = PromptTemplate(
    template="""
You are a helpful assistant.

Answer ONLY from the provided transcript context.

If the context is insufficient, say:
"I don't know based on the transcript."

Use the conversation history when it helps understand follow-up questions.

Previous conversation:
{chat_history}

Transcript context:
{context}

Current question:
{question}
""",
    input_variables=[
        "chat_history",
        "context",
        "question"
    ]
)

def format_docs(docs):
    return "\n\n".join(
        doc.page_content
        for doc in docs
    )

def format_chat_history(chat_history):
    return "\n".join(
    f"User: {user_message}\nAI: {ai_message}"
    for user_message, ai_message in chat_history
)


## Chain

chain = (
    RunnableParallel(
        context=( 
            RunnableLambda(lambda x: x["question"]) | retriever | RunnableLambda(format_docs)
        ),
        question=RunnableLambda( lambda x: x["question"] ),
        chat_history=RunnableLambda( lambda x: format_chat_history(x["chat_history"]) )
    )
    | prompt
    | chat_model
    | StrOutputParser()
)


## CONVERSATION LOOP

chat_history = []

print("\n========================================")
print("YouTube Transcript Chatbot")
print("Using Hugging Face + Gemma 4")
print("Type 'exit' to end the conversation.")
print("========================================\n")


while True:

    question = input("You: ").strip()

    if question.lower() == "exit":
        break

    if not question:
        continue

    answer = chain.invoke({
        "question": question,
        "chat_history": chat_history
    })

    print(f"AI: {answer}\n")

    chat_history.append(
        (question, answer)
    )