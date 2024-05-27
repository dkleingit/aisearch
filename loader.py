import os

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

from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter

loader = DirectoryLoader("data/", glob="*.txt", loader_cls=TextLoader, loader_kwargs={'autodetect_encoding': True})

documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

vector_store.add_documents(documents=docs)