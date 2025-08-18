from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
import os
# Chat template

chat_prompt_template = ChatPromptTemplate([
    ('system','you are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{querry}')
]) 


#load chat history
chat_history = []
Current_working_directory =os.getcwd()
with open(Current_working_directory+'\\prompts\\chat_history.txt') as f:
    chat_history.extend(f.readlines())

# create prompt

prompt = chat_prompt_template.invoke({'chat_history':chat_history,'querry':'where is my refund'})

print(prompt)