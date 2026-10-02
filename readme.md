# LangChain Learning Journey 🦜🔗

This repository contains my **hands-on learning journey with LangChain and LLM application development**.

I'm learning LangChain from the fundamentals and gradually moving toward building real-world AI applications. The goal of this repository is to **understand how things work internally**, not just copy code from tutorials.

---

## 🎯 Goal

I'm using this repository to document what I learn about:

* Large Language Models (LLMs)
* Chat Models
* Prompt Engineering
* Output Parsers
* Chains
* Runnables
* Embeddings
* Vector Databases
* RAG (Retrieval-Augmented Generation)
* Agents
* Tool Calling
* AI Application Development

---

## 📚 What I'm Learning

### 1. LLMs

Learning the fundamentals of interacting with language models through LangChain.

Currently exploring:

* `HuggingFaceEndpoint`
* Hugging Face models
* OpenAI models
* `ChatOpenAI`
* `ChatHuggingFace`
* Model invocation with `.invoke()`
* Understanding model input and output

📁 [`LLMs/`](./LLMs)

---

### 2. Chat Models

Understanding how chat-based models work with structured messages.

Learning:

* `SystemMessage`
* `HumanMessage`
* `AIMessage`
* Chat history
* Message formatting
* Multi-turn conversations

📁 [`ChatModels/`](./ChatModels)

---

### 3. Prompts

Learning how to create reusable and dynamic prompts.

Learning:

* `PromptTemplate`
* Input variables
* Partial variables
* Prompt composition
* Prompt design

📁 [`LangChain_prompts/`](./LangChain_prompts)

---

### 4. Output Parsers

Learning how to convert raw LLM responses into useful structured data.

Exploring:

* `StrOutputParser`
* `PydanticOutputParser`
* `Pydantic` models
* Structured output
* Response schemas

📁 [`LangChain_Output_Parser/`](./LangChain_Output_Parser)

---

### 5. Chains

Learning how LangChain components can be connected together to create pipelines.

Currently exploring:

* LCEL
* Pipe operator (`|`)
* `RunnableParallel`
* `RunnableBranch`
* `RunnableLambda`
* Sequential chains
* Conditional execution
* Passing data between components

📁 [`LangChain_Chains/`](./LangChain_Chains)

---

### 6. Embeddings

Understanding how text can be converted into numerical representations and how those representations are used in AI applications.

Learning:

* Embeddings
* Semantic similarity
* Vector representations
* Vector stores

📁 [`EmbeddingModels/`](./EmbeddingModels)

---

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

* Python
* LangChain
* OpenAI API
* Hugging Face
* Pydantic
* Python-dotenv

More technologies will be added as I progress through the learning journey.

---

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
* [ ] Vector Databases
* [ ] Retrieval
* [ ] RAG
* [ ] Agents
* [ ] Tool Calling
* [ ] Memory
* [ ] Evaluation
* [ ] Production AI Applications

---

## 🗂️ Repository Structure

```text
langChain/
│
├── LLMs/
├── ChatModels/
├── EmbeddingModels/
├── LangChain_prompts/
├── LangChain_Output_Parser/
├── LangChain_Chains/
│
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
