import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.azuresearch import AzureSearch

class AzureSearchSetup:
    def __init__(self):
        load_dotenv()
        self.openai_api_key = os.environ["OPENAI_API_KEY"]
        self.vector_store_address = os.environ["AZURE_AI_SEARCH_ADDRESS"]
        self.vector_store_key = os.environ["AZURE_AI_SEARCH_KEY"]
        self.embeddings = self._create_embeddings()
        self.vector_store = self._create_vector_store()

    def _create_embeddings(self):
        return OpenAIEmbeddings(
            openai_api_key=self.openai_api_key,
            openai_api_version="2023-05-15",
            model="text-embedding-ada-002"
        )

    def _create_vector_store(self):
        return AzureSearch(
            azure_search_endpoint=self.vector_store_address,
            azure_search_key=self.vector_store_key,
            index_name="vector-index",
            embedding_function=self.embeddings.embed_query,
        )