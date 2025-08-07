import os
from dotenv import load_dotenv

from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    PromptTemplate,
    Settings,
)
# Corrected imports for Google's models
from llama_index.llms.google_genai import GoogleGenerativeAI
from llama_index.embeddings.google_genai import GoogleGenerativeAIEmbedding
from llama_index.core.query_engine import RetrieverQueryEngine

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def create_query_engine():
    # Corrected class name for the embedding model
    Settings.llm = GoogleGenerativeAI(api_key=GOOGLE_API_KEY, model="models/gemini-pro", temperature=0)
    Settings.embed_model = GoogleGenerativeAIEmbedding(api_key=GOOGLE_API_KEY)

    documents = SimpleDirectoryReader(input_files=["resume.txt"]).load_data()

    index = VectorStoreIndex.from_documents(documents)

    with open("prompt_template.txt", "r") as f:
        prompt_template_str = f.read()
    prompt = PromptTemplate(prompt_template_str)

    retriever = index.as_retriever(similarity_top_k=2)

    query_engine = RetrieverQueryEngine.from_args(
        retriever=retriever,
        text_qa_template=prompt
    )

    return query_engine