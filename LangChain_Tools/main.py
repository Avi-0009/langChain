from dotenv import load_dotenv
from langchain.agents import create_agent

from langchain_huggingface import (
    HuggingFaceEndpoint,
    ChatHuggingFace
)

from tools.web_search_tool import web_search
from tools.github_tool import get_github_repo
from tools.vercel_tool import get_vercel_deployments
from tools.weather_tool import get_weather


load_dotenv()


# Model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-4-31B-it",
    task="conversational",
    temperature=0.2,
    max_new_tokens=512
)

model = ChatHuggingFace(llm = llm)


# Register tool
tools = [
    get_vercel_deployments,
    get_github_repo,
    get_weather,
    web_search
]


# Create Agent
agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""
You are a helpful AI assistant.

Use tools whenever external or current information is required.

Available tools:

1. Vercel
   Use it for Vercel deployment information.

2. GitHub
   Use it for public GitHub repository information.

3. Weather
   Use it for current weather information.

4. Web Search
   Use it whenever current information from the internet is required.

Never invent information that should come from a tool.
Always use the appropriate tool when necessary.
"""
)


# Chat
messages = []

print("\n========================================")
print("LangChain Tool Calling Agent")
print("Using Hugging Face + Gemma 4")
print("Type 'exit' to end the conversation.")
print("========================================\n")


while True:

    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        break

    if not user_input:
        continue

    messages.append({
        "role": "user",
        "content": user_input
    })

    try:

        result = agent.invoke({
            "messages": messages
        })

        messages = result["messages"]

        print(f"\nAI: {messages[-1].content}\n")

    except Exception as e:

        print(f"\nError: {e}\n")


print("\nConversation ended.")