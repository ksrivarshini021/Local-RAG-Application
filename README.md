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
`git clone `
