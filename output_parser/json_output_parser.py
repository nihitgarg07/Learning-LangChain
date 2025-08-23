from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser




# load api key
load_dotenv()

# Use HuggingFaceEndpoint directly to call the repo
llm = HuggingFaceEndpoint(
    model="google/gemma-2-2b-it",
    task="text-generation"
)

# now passing it in the chathuggingface interface
model = ChatHuggingFace(llm=llm)

#creating parser
parser = JsonOutputParser()

# 1st prompt - > detailed report
template1 = PromptTemplate(
    template='give me the name, age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
    )



# prompt = template1.format()

# result = model.invoke(prompt)

# final_Reslt = parser.parse(result.content)

""" or we can use chain inreplace of above code"""

chains = template1 | model | parser
result = chains.invoke({})
print(result)