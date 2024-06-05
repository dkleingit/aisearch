from langchain.chains import ConversationalRetrievalChain
from langchain_openai.chat_models import ChatOpenAI

class ConversationalRetrieval:
    def __init__(self, vector_store):
        self.chain = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(model="gpt-3.5-turbo"),
            retriever=vector_store.as_retriever(),
        )
        self.chat_history = []

    def process_query(self, query):
        result = self.chain.invoke({"question": query, "chat_history": self.chat_history})
        self.chat_history.append((query, result['answer']))
        return result['answer']

    def start_chat(self):
        query = None
        while True:
            if not query:
                query = input("Prompt: ")
            if query in ['quit', 'q', 'exit']:
                import sys
                sys.exit()
            answer = self.process_query(query)
            print(answer)
            query = None