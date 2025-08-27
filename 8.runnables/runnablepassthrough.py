from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence , RunnableParallel ,RunnablePassthrough


load_dotenv()

prompt1 = PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explan the following joke {text}',
    input_variables=['text']
)

model = ChatOpenAI()
parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel(
    {
        'joke' : RunnablePassthrough(),
        'joke_Explaination' : RunnableSequence(prompt2,model,parser)

    }
)

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

print(final_chain.invoke({'topic','cricket'}))