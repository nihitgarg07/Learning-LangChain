from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


# Loading the Api key fro .env file
load_dotenv()


# Creating an embedding model with specifing model and dimension
embedding = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)


# passing querry to the model and storing in the result
result =embedding.embed_query("Delhi is capital of India")

# printing result
print(result)