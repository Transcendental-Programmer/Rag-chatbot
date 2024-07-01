from data_processing import get_processed_data
from vector_store import initialize_vector_store
from qa_chain import create_qa_chain
from api import run_api

def main():
    processed_data = get_processed_data()
    print("Processed data:")

    vector_store = initialize_vector_store(processed_data)
    print("Initialized vector store")
    
    qa_chain = create_qa_chain(vector_store)
    print("Created QA chain")

    print("Running API")
    run_api(qa_chain)

if __name__ == "__main__":
    main()