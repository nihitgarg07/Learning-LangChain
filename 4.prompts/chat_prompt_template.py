from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


# Do Not send in this way in Chat_prompt_template

"""
chat_template = ChatPromptTemplate([
    SystemMessage(content='you are a helpful {domain} expert'),
    HumanMessage(content='Explain in simple terms , what is {topic}')
])

"""

chat_template = ChatPromptTemplate([

    ('system','you are a helpful {domain} expert'),
    ('human','Explain in simple terms, what is {topic}')
    
])


prompt = chat_template.invoke({'domain' : 'cricket',
                               'topic' : 'Dusra'})

