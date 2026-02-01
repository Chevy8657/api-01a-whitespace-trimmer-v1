import re
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI(title="Whitespace Trimmer", version="v1")

class Health(BaseModel):
    ok: bool

class WhitespaceTrimResponse(BaseModel):
    input: str
    trimmed: str
    original_length: int
    trimmed_length: int

@app.get("/health", response_model=Health)
def health():
    return {"ok": True}

@app.get("/v1/whitespace-trim", response_model=WhitespaceTrimResponse)
def whitespace_trim(text: str = Query(..., description="Text to trim/normalize whitespace")):
    original = text
    trimmed = re.sub(r"\s+", " ", original.strip())
    return {
        "input": original,
        "trimmed": trimmed,
        "original_length": len(original),
        "trimmed_length": len(trimmed),
    }
