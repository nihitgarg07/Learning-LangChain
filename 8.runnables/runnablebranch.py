from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence , RunnableParallel ,RunnablePassthrough , RunnableLambda , RunnableBranch



load_dotenv()

prompt1 = PromptTemplate(
    template='write a report on the topic about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='summarize the following text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI()
parser = StrOutputParser()


report_gen_chain = RunnableSequence(prompt1,model,parser)

branch_chain = RunnableBranch(
    (lambda x:len(str(x).split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain,branch_chain)

result = final_chain.invoke({'topic':'Russia vs Ukraine'})

print(result)

