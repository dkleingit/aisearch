import os
import sys

from dotenv import load_dotenv
from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_openai import OpenAIEmbeddings

load_dotenv()

openai_api_key: str = os.environ["OPENAI_API_KEY"] 
openai_api_version: str = "2023-05-15"
model: str = "text-embedding-ada-002"

vector_store_address: str = os.environ["AZURE_AI_SEARCH_ADDRESS"]
vector_store_password: str = os.environ["AZURE_AI_SEARCH_PWD"]

embeddings: OpenAIEmbeddings = OpenAIEmbeddings(
    openai_api_key=openai_api_key, openai_api_version=openai_api_version, model=model
)

index_name: str = "vector-index"
vector_store: AzureSearch = AzureSearch(
    azure_search_endpoint=vector_store_address,
    azure_search_key=vector_store_password,
    index_name=index_name,
    embedding_function=embeddings.embed_query,
)

from langchain.chains import ConversationalRetrievalChain
from langchain_openai.chat_models import ChatOpenAI

chain = ConversationalRetrievalChain.from_llm(
  llm=ChatOpenAI(model="gpt-3.5-turbo"),
  retriever=vector_store.as_retriever(),
)

query = None  
chat_history = []
while True:
  if not query:
    query = input("Prompt: ")
  if query in ['quit', 'q', 'exit']:
    sys.exit()
  result = chain.invoke({"question": query, "chat_history": chat_history})
  print(result['answer'])

  chat_history.append((query, result['answer']))
  query = None
