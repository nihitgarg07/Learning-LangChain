import random


# Create a dummy LLM that is giving random response from list
class NakliLLM:
    def __init__(self):
        pass

    def predict(self,prompt):
        response_list =[
            'Delhi is the capital of India',
            'IPL is a cricket leagure',
            'AI stands for Artifitial Intelligence'
        ]

        return {'response': random.choice(response_list)}


# llm = NakliLLM()
# print(llm.predict('What is the capital of india'))


# Create a dummy prompttemplate class
class NakliPromptTemplate:

    def __init__(self,template,input_variables):
        self.template = template
        self.input_variable = input_variables

    def format(self,input_dict):
        return self.template.format(**input_dict) 

template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['topic']
)       

# prompt = template.format({'length':'short','topic':'india'})

llm = NakliLLM()
# llm.predict(prompt)

# Created a LLM Chain
class NakliLLMChain:
    def __init__(self,llm,prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self,input_dict):

        final_prompt = self.prompt.format(input_dict)  
        result = self.llm.predict(final_prompt)
        return result['response']

chain = NakliLLMChain(llm,template)

print(chain.run({'length':'short','topic':'india'}))