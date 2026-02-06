# file: query_rag.py
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

PERSIST_DIR = "./chroma-store"

# 1. Reload vector store
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=OPENAI_API_KEY,
)

vectorstore = Chroma(
    persist_directory=PERSIST_DIR,
    embedding_function=embeddings,
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# 2. LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    api_key=OPENAI_API_KEY,
)

# 3. Prompt
prompt = ChatPromptTemplate.from_template(
    """You are a helpful assistant.
Use the provided context to answer the question.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{question}
"""
)

# 4. LCEL RAG chain
rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)

def ask(query: str):
    print("\nQ:", query)
    answer = rag_chain.invoke(query)
    print("\nA:", answer)

if __name__ == "__main__":
    ask("Explain RAG to a junior backend developer.")
