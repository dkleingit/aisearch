from search_setup import AzureSearchSetup
from document_processing import DocumentProcessor

def main():
    azure_setup = AzureSearchSetup()
    vector_store = azure_setup.vector_store

    doc_processor = DocumentProcessor("data/")
    documents = doc_processor.load_and_split_documents()
    vector_store.add_documents(documents=documents)

if __name__ == "__main__":
    main()