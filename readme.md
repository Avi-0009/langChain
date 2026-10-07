# LangChain Learning Journey 🦜🔗

This repository contains my **hands-on learning journey with LangChain and LLM application development**.

I'm learning LangChain from the fundamentals and gradually moving toward building real-world AI applications. The goal of this repository is to **understand how things work internally**, not just copy code from tutorials.

---

## 🎯 Goal

I'm using this repository to document what I learn about:

- Large Language Models (LLMs)
- Chat Models
- Prompt Engineering
- Output Parsers
- Chains
- Runnables
- Embeddings
- Vector Databases
- Retrievers
- RAG (Retrieval-Augmented Generation)
- Agents
- Tool Calling
- AI Application Development

---

## 📚 What I'm Learning

### 1. LLMs

Learning the fundamentals of interacting with language models through LangChain.

Currently exploring:

- `HuggingFaceEndpoint`
- Hugging Face models
- OpenAI models
- `ChatOpenAI`
- `ChatHuggingFace`
- Model invocation with `.invoke()`
- Understanding model input and output
- Conversational LLM usage

📁 [`LLMs/`](./LLMs)

---

### 2. Chat Models

Understanding how chat-based models work with structured messages.

Learning:

- `SystemMessage`
- `HumanMessage`
- `AIMessage`
- Chat history
- Message formatting
- Multi-turn conversations
- OpenAI chat models
- Hugging Face chat models

📁 [`ChatModels/`](./ChatModels)

---

### 3. Prompts

Learning how to create reusable and dynamic prompts.

Learning:

- `PromptTemplate`
- Input variables
- Partial variables
- Prompt composition
- Prompt design

📁 [`LangChain_Prompts/`](./LangChain_Prompts)

---

### 4. Output Parsers

Learning how to convert raw LLM responses into useful structured data.

Exploring:

- `StrOutputParser`
- `PydanticOutputParser`
- `Pydantic` models
- Structured output
- Response schemas

📁 [`LangChain_Output_Parser/`](./LangChain_Output_Parser)

---

### 5. Chains

Learning how LangChain components can be connected together to create pipelines.

Currently exploring:

- LCEL
- Pipe operator (`|`)
- `RunnableParallel`
- `RunnableBranch`
- `RunnableLambda`
- Sequential chains
- Conditional execution
- Passing data between components

📁 [`LangChain_Chains/`](./LangChain_Chains)

---

### 6. Embeddings

Understanding how text can be converted into numerical representations and how those representations are used in AI applications.

Learning:

- Embeddings
- Semantic similarity
- Vector representations
- Embedding models
- Sentence Transformers
- Vector stores

📁 [`EmbeddingModels/`](./EmbeddingModels)

---

### 7. Vector Databases

Learning how embeddings can be stored and searched using vector databases.

Currently explored:

- Chroma
- FAISS
- Local persistent Chroma databases
- Document storage
- Metadata
- Stable document IDs
- Similarity search
- Metadata filtering
- Updating documents
- Vector store operations

📁 [`LangChain_VectorDatabase/`](./LangChain_VectorDatabase)

The Chroma examples use a local persistent database that is intentionally excluded from Git using `.gitignore`.

---

### 8. Retrievers

Learning how LangChain retrieves relevant documents from a vector store based on a query.

Currently exploring:

- Similarity Retriever
- MMR Retriever
- Multi-Query Retriever
- Contextual Compression Retriever
- Document retrieval
- Query transformation
- Retrieval optimization
- LLM-based document compression

📁 [`LangChain_Retrievers/`](./LangChain_Retrievers)

## 🧠 Learning Approach

I'm following a simple approach:

```text
Learn the concept
      ↓
Understand what happens internally
      ↓
Implement it with LangChain
      ↓
Experiment with different models
      ↓
Build something practical
```

This repository is intentionally **incremental**. Some examples are small because the purpose is to understand individual LangChain concepts before combining them into larger applications.

---

## 🛠️ Tech Stack

- Python
- LangChain
- LangChain classic
- LangChain Community
- OpenAI API
- Hugging Face
- Chroma
- FAISS
- Pydantic
- Python-dotenv
- SQLite (used internally by local Chroma persistence)

More technologies will be added as I progress through the learning journey.

---

### 9. Tools & Agents

Learning how LLMs can interact with external systems and APIs through tools.

Currently exploring:

- Custom LangChain tools using `@tool`
- Vercel API integration
- GitHub API integration
- Weather API integration
- Web search
- Tool selection by the LLM
- Agent-based tool execution
- Multi-turn conversations with tools
- `create_agent`
- Hugging Face + Gemma 4 for tool calling

📁 [`LangChain_Tools/`](./LangChain_Tools)

Current tool architecture:

```text
User
  ↓
Gemma 4
  ↓
Agent
  ├── Vercel API
  ├── GitHub API
  ├── Weather API
  └── Web Search
  ↓
Tool Result
  ↓
Gemma 4
  ↓
Final Response
```

## 📈 Progress

* [x] LLM basics
* [x] OpenAI integration
* [x] Hugging Face integration
* [x] Chat Models
* [x] System / Human / AI Messages
* [x] Prompt Templates
* [x] Output Parsers
* [x] Pydantic Output Parsing
* [x] Basic Chains
* [x] Runnable Parallel
* [x] Runnable Branch
* [x] Runnable Lambda
* [x] Embedding Models
* [x] Vector Databases
* [x] Chroma
* [x] FAISS
* [x] Retrieval
* [x] Similarity Retriever
* [x] MMR Retriever
* [x] Multi-Query Retriever
* [x] Contextual Compression Retriever
* [x] RAG basics
* [x] Tool Calling
* [x] API Tools
* [x] Web Search
* [ ] Advanced Agents
* [ ] Memory
* [ ] Evaluation
* [ ] Production AI Applications

---

## 🗂️ Repository Structure

```text
LangChain/
│
├── ChatModels/
├── EmbeddingModels/
├── LangChain_Chains/
├── LangChain_Output_Parser/
├── LangChain_Prompts/
├── LangChain_Retrievers/
├── LangChain_Tools/
│   ├── LangChain_Tools/
│   │   ├── github_tool.py
│   │   ├── vercel_tool.py
│   │   ├── weather_tool.py
│   │   └── web_search_tool.py
│   └── main.py
│
├── LangChain_VectorDatabase/
│   ├── Chroma_DB/        # Local database, ignored by Git
│   └── langChainChroma.py
│
├── LLMs/
│
├── .env                 # Ignored by Git
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Why This Repository Exists

This isn't meant to be a single finished project.

It's my **learning log and implementation repository for LangChain**.

I'll keep adding examples as I learn new concepts, experiment with different LLM providers, and move from basic LLM calls toward more advanced AI systems such as **RAG and AI agents**.

---

⭐ This repository will evolve as I learn more.
