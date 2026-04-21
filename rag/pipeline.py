from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.llms.openai import OpenAI
from qdrant_client import QdrantClient
from rag.config import QDRANT_URL, COLLECTION_NAME

def query_rag(user_query: str):
    client = QdrantClient(url=QDRANT_URL)
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
    )
    index = VectorStoreIndex.from_vector_store(vector_store)
    llm = OpenAI(model="gpt-4o-mini", temperature=0)
    query_engine = index.as_query_engine(
        llm=llm,
        similarity_top_k=2
    )
    response = query_engine.query(user_query)
    return {
        "answer": str(response),
        "sources": [
            node.get_text()
            for node in getattr(response, "source_nodes", [])
        ]
    }