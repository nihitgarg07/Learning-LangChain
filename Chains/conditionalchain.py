from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel ,RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal, cast

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)    

prompt1 = PromptTemplate(
    template='Classify the sentimenet of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}

)


classfier_chain = prompt1 | model | parser2

print(classfier_chain.invoke({'feedback':'this is a terrible smartphone'}).sentiment)




prompt2 = PromptTemplate(
    template='write an appropriate response to this positive feedback\n {feedback}',
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template='write an appropriate response to this Negative feedback\n {feedback}',
    input_variables=['feedback']
)

"""
with the below runnable branch it is just like below if else code
branch_chain = RunnableBranch(
    (condition1 , chain1),
    (condition2, chain2),
    default chain
)
"""



branch_chain = RunnableBranch(
    (lambda x: cast(Feedback, x).sentiment == "positive" , prompt2 | model | parser),
    (lambda x: cast(Feedback, x).sentiment == 'negative' , prompt3 | model | parser),
    RunnableLambda(lambda x: 'could not find sentiment') # Here we have converted this lambda function to runnable lamda as it is not a chain
)

final_chain = classfier_chain | branch_chain

final_result = final_chain.invoke({'feedback':'This is a terrible phone'})

print(final_result)