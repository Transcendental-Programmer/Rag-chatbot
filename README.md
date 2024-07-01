# RAG Chatbot

This project implements a Retrieval-Augmented Generation (RAG) chatbot using the Hugging Face API, PINECONE DB.

## Images
### homepage
![homepage](https://github.com/Transcendental-Programmer/Rag-chatbot/blob/main/static/home.png)
### chatpage
![chat page](https://github.com/Transcendental-Programmer/Rag-chatbot/blob/main/static/chat.png)
## Prerequisites

- Python 3.11.4
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Transcendental-Programmer/Rag-chatbot.git
   cd Rag-chatbot
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv myenv
   myenv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Sign up for a Hugging Face account if you haven't already: https://huggingface.co/join

2. Generate an API token from your Hugging Face account settings.

3. Create a `.env` file in the project root directory and add your Hugging Face API token and pinecone api:
   ```
   HUGGINGFACE_API_TOKEN=your_api_token_here
   PINECONE_API_KEY=your_ api
   ```

## Usage

1. run the main script:
   ```
   python main.py
   ```

2. The server will start running on `http://localhost:5000`.

3. To query the chatbot, send a POST request to `http://localhost:5000/query` with a text message.
   

## Troubleshooting

If you encounter an "Invalid token" error:

1. Verify your Hugging Face API token in your account settings.
2. Ensure the token in your `.env` file is correct and up-to-date.
3. Check that you have the necessary permissions to access the model (google/flan-t5-base).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
