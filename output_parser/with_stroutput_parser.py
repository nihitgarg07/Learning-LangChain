from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


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

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)