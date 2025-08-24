from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv


# Loading the Api key fro .env file
load_dotenv()

# Creating a connect to hugging face repo
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-4B-Thinking-2507",
    task="text-generation"
)

# Creating an object and wrapping a LLM model to hugging face object
model = ChatHuggingFace(llm=llm)

# giving a prompt to a model
result = model.invoke("What is the capital of india ?")

# printing result
print(result)
