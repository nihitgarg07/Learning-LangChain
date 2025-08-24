from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline


# download the HuggingFace repo with certain model to you local
llm= HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen3-4B-Thinking-2507",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens=50
    )
)

# Creating ChatHuggingFace object which is interacting wit the llm
model = ChatHuggingFace(llm = llm)
result = model.invoke("what is the capital of india ?")
print(result)