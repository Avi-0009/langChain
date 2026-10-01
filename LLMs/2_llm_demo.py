import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(api_key=os.getenv("HUGGING_FACE_API_KEY"))

response = client.chat.completions.create(
    model="google/gemma-4-31B-it",
    messages=[{"role": "user", "content": "Write a short poem about coding."}],
    max_tokens=200,
)

print(response.choices[0].message.content)