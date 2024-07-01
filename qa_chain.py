from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEndpoint
from config import HUGGINGFACEHUB_API_TOKEN

def create_qa_chain(vector_store):
    llm = HuggingFaceEndpoint(
        repo_id="google/flan-t5-base",
        temperature=0.5,  
        model_kwargs={"max_length": 512},
        huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN
    )
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(),
        return_source_documents=True
    )
    
    return qa_chain
