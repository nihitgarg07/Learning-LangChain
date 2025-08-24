from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Loading the Api key fro .env file
load_dotenv()


# Creating ChatOpenAi object which is uing gpt-4 repo
chatmodel = ChatOpenAI(model='gpt-4',temperature=0,max_completion_tokens=10)

# giving prompt to the model
result = chatmodel.invoke('What is the capital of India ? ')

# prinitng result
print(result)

