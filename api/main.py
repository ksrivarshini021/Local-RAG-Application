import os
from fastapi import FastAPI, UploadFile, File
from rag.ingestion import ingest_file
from rag.pipeline import query_rag

app = FastAPI()

os.makedirs("data", exist_ok=True)

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        file_path = f"data/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())
        ingest_file(file_path)
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

@app.post("/query")
async def query(payload: dict):
    user_query = payload.get("query")

    if not user_query:
        return {"error": "query missing"}

    return query_rag(user_query)