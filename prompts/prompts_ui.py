import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate,load_prompt
import os

# load the api key
load_dotenv()

# build an object for your model
model = ChatOpenAI(model='gpt-4',temperature=0)


# give the header to your UI
st.header("Researh tool")


# INPUT from users for paper_input, style_input , length_input
paper_input = st.selectbox("Select Research Paper Name",["Attention is all you need",
                                                         "BERT: Pre-Training of Deep Bidirectional Transformers",
                                                         "GPT-3: Language Models are few shot Learnders",
                                                         "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explaination Style",["Beginner Friendly",
                                                        "Technical","Code Oriented","Mathemetical"])

length_input = st.selectbox("Select Explaination Lengt",["Short (1-2 paragraphs)","Medium(3-5 paragraphs)",
                                                         "Long (detailed Explaination)"])


# fetching current working directory
Current_working_directory =os.getcwd()

#load tempalte
template = load_prompt(Current_working_directory+'/prompts/template.json')

# set the input in template and saving it in prompt
prompt= template.invoke({
"paper_input" : paper_input,
"style_input" : style_input,
"length_input": length_input

})

# passing the prompt in model on the press of summarize button
if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)
   
    