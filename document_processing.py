from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter

class DocumentProcessor:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def load_and_split_documents(self):
        loader = DirectoryLoader(self.directory_path, glob="*.txt", loader_cls=TextLoader, loader_kwargs={'autodetect_encoding': True})
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        return text_splitter.split_documents(documents)