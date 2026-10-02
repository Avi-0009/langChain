from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import (
    RunnableParallel, 
    RunnableBranch, 
    RunnableLambda
)
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

# Models
model1 = ChatOpenAI()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-4-31B-it",
    task="text-generation"
)

model2 = ChatHuggingFace(llm = llm)

# Output schema
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser1 = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

# Sentiment classification prompt
prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

# Classification chain
classifier_chain = prompt1 | model2 | parser2

# Response prompts
prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

# Preserve original feedback with classification
full_chain = RunnableParallel(
    feedback=RunnableLambda(lambda x: x['feedback']),
    sentiment=classifier_chain
)

#Branch
branch_chain = RunnableBranch(
    (
        lambda x: x["sentiment"].sentiment == "positive",
        prompt2 | model1 | parser1
    ),
    (
        lambda x: x["sentiment"].sentiment == "negative",
        prompt3 | model1 | parser1
    ),
    RunnableLambda(lambda x: "Could not find sentiment")
)

chain = full_chain | branch_chain

result = chain.invoke({'feedback': 'This is a terrible world, everyone kept exploiting this world!'})

print(result)
