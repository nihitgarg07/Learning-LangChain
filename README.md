# LangChain Models – Learning Snippets

This repository contains small, focused code snippets and experiments for learning and practicing **LangChain** concepts, including:

- 🔹 Chat Models (OpenAI, Hugging Face)
- 🔹 Embedding Models (OpenAI, Local)
- 🔹 LLMs and prompt interaction

---

## 📁 Folder Structure

LANGCHAIN_MODELS/
│
├── ChatModels/
│ ├── chatmodel_openai.py # Using OpenAI's chat models (ChatOpenAI)
│ ├── huggingface_local.py # Running local HF models as chat models
│ └── huggingface_api.py # Using HF endpoint-based chat models
│
├── EmbeddedModels/
│ ├── embedding_hf_local.py # Local Hugging Face embeddings
│ ├── embeddings_openai_docs.py # OpenAI embeddings for documents
│ └── embeddings_openai_querry.py # Query-based embedding use
│
├── LLMs/
│ └── llm_demo.py # Basic LLM interaction examples
│
├── .env # Environment variables (API keys etc.)
├── .gitignore # Ignoring sensitive or unnecessary files
├── requirements.txt # Python dependencies
└── README.md # You're here!


## 🧠 Purpose

This repo is part of my **LangChain learning journey**, where I:

- Follow tutorials and official docs
- Build small hands-on examples
- Organize and version my learning

---

## 🚀 Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/langchain-models-learning.git
   cd langchain-models-learning

Install dependencies

pip install -r requirements.txt
Set your environment variables in .env


OPENAI_API_KEY=your_openai_key
HUGGINGFACEHUB_API_TOKEN=your_hf_token


Run a script
python ChatModels/chatmodel_openai.py



# Tools & Libraries

LangChain

OpenAI

Hugging Face

Python


📌 Notes

These scripts are minimal examples meant to isolate and understand each feature.

Some files may overlap or experiment with the same concept in different ways.