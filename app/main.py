from fastapi import FastAPI
from pydantic import BaseModel
from app.bigram_model import BigramModel
import spacy


app = FastAPI()

corpus = [
    "The Count of Monte Cristo is a novel written by Alexandre Dumas. "
    "It tells the story of Edmond Dantès, who is falsely imprisoned and later seeks revenge.",
    "We are generating text based on bigram probabilities.",
    "Bigram models are simple but effective."
]

bigram_model = BigramModel(corpus)

class TextGenerationRequest(BaseModel):
    start_word: str
    length: int

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate")
def generate_text(request: TextGenerationRequest):
    generated = bigram_model.generate_text(request.start_word, request.length)
    return {"generated_text": generated}

nlp = spacy.load("en_core_web_lg")

class EmbeddingRequest(BaseModel):
    word: str

@app.post("/embedding")
def embedding_api(req: EmbeddingRequest):
    w = req.word.strip()
    if not w:
        return {"error": "empty word"}
    vec = nlp(w).vector
    return {"word": w, "dim": len(vec), "embedding": vec.tolist()}
