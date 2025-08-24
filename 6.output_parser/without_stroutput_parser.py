from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


"""
Code using Hugging face

# load api key
load_dotenv()

# Use HuggingFaceEndpoint directly to call the repo
llm = HuggingFaceEndpoint(
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

# now passing it in the chathuggingface interface
model = ChatHuggingFace(llm=llm)

# 1st prompt - > detailed report
template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
    )
# 2nd prompt -> summary

template2 = PromptTemplate(
    template='write a5 line summary on the following text. /n {text}',
    input_variables=['text']
    )


prompt1 = template1.invoke({'topic':'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result2 = model.invoke(prompt2)

print(result2.content)

"""


# load api key
load_dotenv()

# Use chatOpenAi
model = ChatOpenAI()


# 1st prompt - > detailed report
template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
    )
# 2nd prompt -> summary

template2 = PromptTemplate(
    template='write a5 line summary on the following text. /n {text}',
    input_variables=['text']
    )


prompt1 = template1.invoke({'topic':'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result2 = model.invoke(prompt2)

print(result2.content)