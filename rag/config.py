import os
from dotenv import load_dotenv
load_dotenv()
COLLECTION_NAME = os.getenv("QDRANT_COLLECTION")
QDRANT_URL = os.getenv("QDRANT_URL")
OPEN_API_KEY = os.getenv("OPEN_API_KEY")