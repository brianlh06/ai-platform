import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/analyze")
def analyze(text: str):
    api_key = os.getenv("AI_API_KEY", "missing")
    return {
        "text_length": len(text),
        "key_loaded": api_key != "missing",
    }