from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    Settings,
)
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from rag.config import QDRANT_URL, COLLECTION_NAME

# local embedding model
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en"
)

def ingest_file(file_path: str):
    print("Starting ingestion...")

    # 1. Load PDF
    documents = SimpleDirectoryReader(
        input_files=[file_path]
    ).load_data()
    print(f"Loaded {len(documents)} documents")

    # 2. Connect Qdrant
    client = QdrantClient(url=QDRANT_URL)

    # 3. Create collection (SAFE)
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,  # required for bge-small
            distance=Distance.COSINE,
        ),
    )
    print("Collection created")

    # 4. Create vector store
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
    )

    # 5. Storage context
    storage_context = StorageContext.from_defaults(
        vector_store=vector_store
    )

    # 6. Index (this writes to Qdrant)
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
    )

    print("Ingestion complete")