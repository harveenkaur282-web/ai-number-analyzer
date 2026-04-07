from fastapi import FastAPI
from backend.engines import rule_engine
from backend.engines import meme_engine

app = FastAPI()

@app.get("/analyze/{number}")
def analyze(number: int):
    result = rule_engine.analyze(number)
    meme = meme_engine.generate(number)

    return {
        "number": number,
        "even": result["even"],
        "prime": result["prime"],
        "meme": meme
    }