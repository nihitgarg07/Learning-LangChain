from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts abot {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

chains = prompt | model | parser
result = chains.invoke({'topic':'black hole'})
print(result)

chains.get_graph().print_ascii() # to visualize your chain