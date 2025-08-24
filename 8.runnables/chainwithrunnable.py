import random
from abc import ABC,abstractmethod

class Runnable(ABC):

    @abstractmethod
    def invoke(input_data):
        pass


class NakliLLM(Runnable):
    def __init__(self):
        pass

    def invoke(self,prompt):
        response_list =[
            'Delhi is the capital of India',
            'IPL is a cricket leagure',
            'AI stands for Artifitial Intelligence'
        ]

        return {'response': random.choice(response_list)}


    def predict(self,prompt):
        response_list =[
            'Delhi is the capital of India',
            'IPL is a cricket leagure',
            'AI stands for Artifitial Intelligence'
        ]

        return {'response': random.choice(response_list)}


class NakliPromptTemplate(Runnable):

    def __init__(self,template,input_variables):
        self.template = template
        self.input_variable = input_variables

    def invoke(self,input_dict):
        return self.template.format(**input_dict)    

    def format(self,input_dict):
        return self.template.format(**input_dict) 
    
class NakliStrOutputParser(Runnable):
     def __init__(self):
         pass
     
     def invoke(self,input_data):
         return input_data['response']
    

class RunnableConnector(Runnable):
    def __init__(self,runnable_list):
        self.runnable_list = runnable_list

    def invoke(self,input_data):
        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)

        return input_data

template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['topic']
)    

llm = NakliLLM()

parser = NakliStrOutputParser()

chain = RunnableConnector([template,llm,parser])    

print(chain.invoke({'length':'short','topic':'india'}))



"""
In the below code we are passing two chains in the runnable

"""


template1 = NakliPromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
template2 = NakliPromptTemplate(
    template='Explain the following joke {response}',
    input_variables=['response']
)

Chain1 = RunnableConnector([template1,llm])
Chain2 = RunnableConnector([template2,llm,parser])
final_chain = RunnableConnector([Chain1,Chain2])
print(final_chain.invoke({'topic':'cricket'}))