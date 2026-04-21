# Local-RAG-Application

This is a lightweight Retrieval-Arguemnted Generation (RAG) system that could uplaod a document PDFs and could ask questions ina  fully local AI stack

#### Architetcural Flow
The Architecural flow goes as the following

PDF Upload -> LlamaIndex(chunking) -> HuggingFace Embeddings -> Qdrant Vector DB -> Retrieval (top-k chunks) -> Ollama LLM(llama3) -> Answer

#### Tools and Technologies
Backend API- FastAPI
FrontendUI- Streamlit
Vector DB- Qdrant
RAG framework- LlamaIndex
Embeddings- HuggingFace
LLM framework- Ollama
Qdrant container- Docker

#### Setup steps
##### 1. Clone repo
```git clone https://github.com/ksrivarshini021/Local-RAG-Application.git
cd rag-app```

##### 2. Create environment
```uv venv
source .venv/bin/activate```

##### 3. Install dependencies
`uv add fastapi uvicorn streamlit requests python-dotenv
uv add qdrant-client llama-index
uv add llama-index-embeddings-huggingface
uv add llama-index-llms-ollama`

##### 4. Start Qdrant
`docker run -p 6333:6333 qdrant/qdrant`

#### 5. Start Ollama
`ollama serve
ollama pull llama3`

##### 6. Start backend(FastAPI)
`uvicorn api.main:app --reload --port 8080`

##### 7. Start frontend(Streamlit)
`streamlit run app/main.py`


