from search_setup import AzureSearchSetup
from conversational_retrieval import ConversationalRetrieval

def main():
    azure_setup = AzureSearchSetup()
    vector_store = azure_setup.vector_store

    conversational_retrieval = ConversationalRetrieval(vector_store)
    conversational_retrieval.start_chat()

if __name__ == "__main__":
    main()