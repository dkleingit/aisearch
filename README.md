# AI Search

This project demonstrates a system for conversational retrieval using LangChain and OpenAI's GPT-3.5-turbo model. It includes both a command-line interface and a RESTful API for interacting with the system. Additionally, the project utilizes an Azure AI Search resource for efficient document indexing and retrieval.

## Project Structure

my_project/
├── search_setup.py
├── document_processing.py
├── conversational_retrieval.py
├── document_loader.py
├── main.py
├── api_server.py
```

### File Descriptions

- **`search_setup.py`**: Contains the `AzureSearchSetup` class for setting up Azure Search and OpenAI embeddings.
- **`document_processing.py`**: Contains the `DocumentProcessor` class for loading and splitting documents.
- **`conversational_retrieval.py`**: Contains the `ConversationalRetrieval` class for handling the conversational retrieval process.
- **`document_loader.py`**: Script to initialize and add documents to the vector store.
- **`main.py`**: Script for starting an interactive command-line session for conversational retrieval.
- **`api_server.py`**: Script for starting a Flask API server to handle conversational queries.

## Setup and Installation

### 1. Clone the Repository

```sh
git clone https://github.com/dkleingit/aisearch.git
cd aisearch
```

### 2. Install Dependencies

Ensure you have Python 3.7+ installed. Install the required packages using pip:

```sh
pip install -r requirements.txt
```

### 3. Create an Azure AI Search Resource

1. Go to the [Azure Portal](https://portal.azure.com/).
2. Click on **Create a resource**.
3. Search for **AI Search** and select it.
4. Click **Create**.
5. Fill in the required details:
    - **Resource name**: A unique name for your search service.
    - **Subscription**: Your Azure subscription.
    - **Resource group**: Create a new resource group or use an existing one.
    - **Location**: Choose a region close to your location.
    - **Pricing tier**: Select the pricing tier that suits your needs.
6. Click **Review + create**, then **Create**.

Once the Azure AI Search resource is created, find the host address and primary key that is associated with this resource.

### 4. Set Up Environment Variables

Create a `.env` file in the root directory and add the following environment variables:

```
OPENAI_API_KEY=your_openai_api_key
AZURE_AI_SEARCH_ADDRESS=your_azure_search_address
AZURE_AI_SEARCH_PWD=your_azure_search_password
```

- **OPENAI_API_KEY**: Your OpenAI API key.
- **AZURE_AI_SEARCH_ADDRESS**: The endpoint URL of your Azure Cognitive Search service.
- **AZURE_AI_SEARCH_PWD**: The admin key for your Azure Cognitive Search service.

## Usage

### Initializing the Vector Store

Run the `document_loader.py` script to load and split documents, and add them to the Azure vector store:

```sh
python document_loader.py
```

### Command-Line Interface

Run the `main.py` script to start an interactive command-line session:

```sh
python main.py
```

### API Server

Run the `api_server.py` script to start the Flask API server:

```sh
python api_server.py
```

The API server will be running at `http://localhost:5000`.

#### API Endpoint

- **`POST /chat`**

  Request Body:

  ```json
  {
    "query": "Your question here"
  }
  ```

  Response:

  ```json
  {
    "query": "Your question here",
    "answer": "The response from the system"
  }
  ```

### Example API Request

You can send a POST request to the `/chat` endpoint using `curl`:

```sh
curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d '{"query": "What is the capital of France?"}'
```

Response:

```json
{
  "query": "What is the capital of France?",
  "answer": "The capital of France is Paris."
}
```

## License

This project is licensed under the MIT License.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI](https://www.openai.com/)
- [Flask](https://flask.palletsprojects.com/)
- [Azure Cognitive Search](https://azure.microsoft.com/en-us/services/search/)
```

This README provides a comprehensive overview of the project, including setup instructions, usage guidelines, and additional information on licensing and contributions. It also includes detailed steps for creating an Azure AI Search resource.