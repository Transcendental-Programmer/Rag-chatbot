from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import Pinecone
from pinecone import Pinecone as PineconeClient, ServerlessSpec
from config import PINECONE_API_KEY, PINECONE_INDEX_NAME, MODEL_NAME

def initialize_vector_store(texts):
    pc = PineconeClient(api_key=PINECONE_API_KEY)
    
    embeddings = HuggingFaceEmbeddings(model_name=MODEL_NAME)
    
    if PINECONE_INDEX_NAME not in pc.list_indexes().names():
        print(f"Creating new Pinecone index: {PINECONE_INDEX_NAME}")
        try:
            pc.create_index(
                name=PINECONE_INDEX_NAME,
                dimension=384,
                metric='cosine',
                spec=ServerlessSpec(
                    cloud='aws',
                    region='us-east-1'
                )
            )
            print(f"Index {PINECONE_INDEX_NAME} created successfully")
        except Exception as e:
            print(f"Error creating index: {str(e)}")
            return None
    else:
        print(f"Index {PINECONE_INDEX_NAME} already exists")

    try:
        index = pc.Index(PINECONE_INDEX_NAME)
        stats = index.describe_index_stats()
        
        vector_store = Pinecone.from_existing_index(PINECONE_INDEX_NAME, embeddings)
        
        if stats['total_vector_count'] == 0:
            print("Adding texts to the vector store...")
            vector_store.add_texts(texts)
            print("Texts added successfully")
        else:
            print("Vector store already contains data. Skipping text addition.")

        return vector_store
    except Exception as e:
        print(f"Error initializing vector store: {str(e)}")
        return None