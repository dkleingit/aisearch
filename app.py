from flask import Flask, request, jsonify
from azure_setup import AzureSearchSetup
from conversational_retrieval import ConversationalRetrieval

app = Flask(__name__)

# Initialize the vector store and conversational retrieval
azure_setup = AzureSearchSetup()
vector_store = azure_setup.vector_store
conversational_retrieval = ConversationalRetrieval(vector_store)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get('query')
    if not query:
        return jsonify({"error": "Query is required"}), 400

    answer = conversational_retrieval.process_query(query)
    return jsonify({"query": query, "answer": answer})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
