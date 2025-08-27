# LangChain Models – Learning Snippets

This repository contains small, focused code snippets and experiments for learning and practicing **LangChain** concepts, including:

- 🔹 Chat Models (OpenAI, Hugging Face)  
- 🔹 Embedding Models (OpenAI, Local)  
- 🔹 LLMs and Prompt Interaction  
- 🔹 Prompt Templates (JSON-driven)  
- 🔹 Streamlit UI for Prompt Testing  
- 🔹 Messaging & Conversation History (Message Placeholder, Chat Prompts, Chatbot)  
- 🔹 Structured outputs with typedict , pydantic , json_Schema
- 🔹 output parsers with string Output Parser , json output parser , structured output parser , pydantic output parser
- 🔹 chain with sequential , parallel and conditional chains
- 🔹 Runnables ( Sequence , Parallel , Passthrough , lambda , branch )



---

## 🧠 Purpose

This repo is part of my **LangChain learning journey**, where I:

- Follow tutorials and official docs  
- Build small hands-on examples  
- Organize and version my learning  
- Experiment with UI-driven prompt generation  
- Explore conversational flows and message placeholders  

---

## 🚀 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/langchain-models-learning.git
   cd langchain-models-learning

2. Install dependencies

    pip install -r requirements.txt

3. Set your environment variables in .env

    OPENAI_API_KEY=your_openai_key
    HUGGINGFACEHUB_API_TOKEN=your_hf_token

4. Run a script

    python ChatModels/chatmodel_openai.py

5. Run the Streamlit UI

    streamlit run prompts/prompts_ui.py

🛠 Tools & Libraries
    LangChain

    OpenAI

    Hugging Face

    Streamlit

    Python

📌 Notes
    These scripts are minimal examples meant to isolate and understand each feature.

    Some files may overlap or experiment with the same concept in different ways.

    prompts_ui.py lets you test prompts interactively using Streamlit with different styles & lengths.

    chat_prompt_template.py and message_placeholder.py demonstrate how to use message placeholders for injecting conversation history.

    chatbot.py explores a simple chatbot workflow using LangChain’s messaging utilities