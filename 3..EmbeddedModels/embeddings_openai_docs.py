from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


# Loading the Api key fro .env file
load_dotenv()


# Creating an embedding model with specifing model and dimension
embedding = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

# Created a document here
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France "
]

# passing document to the model and storing in the result
result =embedding.embed_documents(documents)

# printing result
for i in result:
    print(i)

