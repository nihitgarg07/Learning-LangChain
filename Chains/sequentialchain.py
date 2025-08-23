from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on the given {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Give me 5 poniter from the given \n {report}",
    input_variables=['report']
)

model = ChatOpenAI()

parser = StrOutputParser()

chains = prompt1 | model | parser | prompt2 | model | parser
result = chains.invoke({'topic':'cricket'})
print(result)

chains.get_graph().print_ascii()