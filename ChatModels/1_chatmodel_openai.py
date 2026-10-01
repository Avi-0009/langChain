from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini', temperature=0.5, max_completion_tokens=20)

result = model.invoke("Tell me about Chat models")
print(result)
print(result.content)