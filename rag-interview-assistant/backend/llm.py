import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI

load_dotenv()

def get_llm():
    return ChatOpenAI(
        temperature=0.7,
        openai_api_key=os.getenv("NVIDIA_API_KEY"),
        openai_api_base="https://xxxx/v1",
        model_name="meta/llama-3.1-8b-instruct"
    )
