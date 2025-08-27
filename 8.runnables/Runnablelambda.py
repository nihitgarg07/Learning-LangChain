from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence , RunnableParallel ,RunnablePassthrough , RunnableLambda



load_dotenv()

def word_count(text):
    return len(text.split())



prompt1 = PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()
parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1,model,parser)

parallet_chain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'word_count' : RunnableLambda(word_count)
    }
)

final_chain = RunnableSequence(joke_gen_chain,parallet_chain)
result = final_chain.invoke({'topic':'AI'})

final_result = """{} \n word count - {}""".format(result['joke'],result['word_count'])


print(final_result)