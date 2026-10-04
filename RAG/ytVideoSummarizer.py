from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_classic.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

## Indexing

# Document Ingestion
video_id = "dQw4w9WgXcQ" # only the YouTube video's id, not the whole URL and use this id if you wanna get Rick rolled

transcript_text = ""

try:
    ytt_api = YouTubeTranscriptApi()

    transcript = ytt_api.fetch(
        video_id,
        languages=["en"]
    )

    # Convert transcript snippets into plain text
    transcript_text = " ".join(
        snippet.text for snippet in transcript
    )

    # print(transcript_text)

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
    chunk_overlap = 100
)
chunks = splitter.create_documents([transcript_text])

# print(chunks[0])

# Embedding generation and storing in Vector store

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorStore = FAISS.from_documents(chunks, embeddings)

## Retriever

retriever = vectorStore.as_retriever(
    search_type="similarity", 
    search_kwargs={"k":4}
)


## LLM

llm = ChatOpenAI(
    model="gpt-4o-mini", 
    temperature=0.2
)

# Prompt
prompt = PromptTemplate(
    template="""
You are a helpful assistant answering questions about a YouTube video.

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
    input_variables=["chat_history", "context", "question"]
)

# Conversation Loop

chat_history = []

print("\n========================================")
print("YouTube Transcript Chatbot")
print("Type 'exit' to end the conversation.")
print("========================================\n")

while True:

    question = input("You: ").strip()

    if question.lower() == "exit":
        break

    if not question:
        continue

    # Retrieve relevant transcript chunks
    retrieved_docs = retriever.invoke(question)

    context_text = "\n\n".join(
        doc.page_content
        for doc in retrieved_docs
    )

    # Convert previous conversation into text
    chat_history_text = "\n".join(
        f"User: {user_message}\nAI: {ai_message}"
        for user_message, ai_message in chat_history
    )

    # Create final prompt
    final_prompt = prompt.invoke({
        "chat_history": chat_history_text,
        "context": context_text,
        "question": question
    })

    # Generate answer
    answer = llm.invoke(final_prompt)

    print(f"AI: {answer.content}\n")

    # Store conversation
    chat_history.append(
        (question, answer.content)
    )


# Final Conversation

print("\n" + "=" * 60)
print("FULL CONVERSATION")
print("=" * 60)

for user_message, ai_message in chat_history:

    print(f"\nYou: {user_message}")
    print(f"AI: {ai_message}")

print("\n" + "=" * 60)
print("Conversation ended.")
print("=" * 60)