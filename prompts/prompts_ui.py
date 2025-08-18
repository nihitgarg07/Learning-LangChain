import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatOpenAI(model='gpt-4',temperature=0)


st.header("Researh tool")

paper_input = st.selectbox("Select Research Paper Name",["Attention is all you need",
                                                         "BERT: Pre-Training of Deep Bidirectional Transformers",
                                                         "GPT-3: Language Models are few shot Learnders",
                                                         "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explaination Style",["Beginner Friendly",
                                                        "Technical","Code Oriented","Mathemetical"])

length_input = st.selectbox("Select Explaination Lengt",["Short (1-2 paragraphs)","Medium(3-5 paragraphs)",
                                                         "Long (detailed Explaination)"])

template = load_prompt('template.json')


prompt= template.invoke({
"paper_input" : paper_input,
"style_input" : style_input,
"length_input": length_input

})

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)
   
    