from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import StructuredOutputParser , ResponseSchema



# load api key
load_dotenv()

# Use HuggingFaceEndpoint directly to call the repo
llm = HuggingFaceEndpoint(
    model="google/gemma-2-2b-it",
    task="text-generation"
)

# now passing it in the chathuggingface interface
model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1',description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2',description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3',description='Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 Facts about the {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser 
result = chain.invoke({'topic':'black hole'})
print(result)

# prompt = template.invoke({'topic':'black hole'})

# result = model.invoke(prompt)

# final_result = parser.parse(str(result.content))

# print(final_result)