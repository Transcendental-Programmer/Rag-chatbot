from flask import Flask, render_template, request, jsonify
from qa_chain import create_qa_chain

app = Flask(__name__)

qa_chain = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')


@app.route('/query', methods=['POST'])
def query():
    data = request.json
    question = data.get('question')
    
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    if qa_chain is None:
        return jsonify({"error": "QA chain not initialized"}), 500
    
    result = qa_chain({"query": question})
    
    return jsonify({
        "answer": result['result'],
        "sources": [doc.page_content for doc in result['source_documents']]
    })


def run_api(chain):
    global qa_chain
    qa_chain = chain
    app.run(debug=True)