from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

# Loading the Api key fro .env file
load_dotenv()

# Making a connection to the hugging face repo 
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# passing your text to create vector and printing the result
text = "Delhi is the capital of India"
vector = embeddings.embed_query(text)
print(vector)

    
