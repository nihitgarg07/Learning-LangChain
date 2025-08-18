from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load API keys in file
load_dotenv()

# create object for chatmodel
model = ChatOpenAI()

# predefined system message and human message
message = [
    SystemMessage(Content ='you are a helpful assistant'),
    HumanMessage(content='Tell me about LangChai')
]

# invoking your mode using message
result = model.invoke(message)

#now append the ai message in messagelist
message.append(AIMessage(content=result.content))

print(message)