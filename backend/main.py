from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.engines import rule_engine, ml_engine, multiverse, global_engine, distributed, bureaucracy, social, meme
from app.schemas import AnalyzeResponse
import asyncio

app = FastAPI(title="OmniNumberAnalyzer v2.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/analyze")
async def analyze(number: int) -> AnalyzeResponse:
    logs = []

    # Layer 1: Distributed simulation
    logs += await distributed.simulate(number)

    # Layer 2: Bureaucracy
    logs += await bureaucracy.process(number)

    # Layer 3: Global API fetch
    global_results = await global_engine.fetch_all(number)
    logs += global_results["logs"]

    # Layer 4: ML prediction
    ml_pred = ml_engine.predict(number)

    # Layer 5: Rule-based ground truth
    is_even = rule_engine.check_even(number)
    is_prime = rule_engine.check_prime(number)

    # Layer 6: Multiverse voting
    mv = multiverse.decide(ml_pred, is_even, global_results["votes"])
    logs += mv["logs"]

    # Layer 7 & 8: Meme + social
    social_out = social.analyze(number)
    meme_out = meme.generate(number)

    return AnalyzeResponse(
        number=number, even=is_even, prime=is_prime,
        ml_prediction=ml_pred, multiverse_decision=mv["verdict"],
        confidence=mv["confidence"], logs=logs,
        meme_output=meme_out, social_output=social_out,
        status=mv["status"]
    )

@app.get("/global-engine/{country}")
async def country_analysis(country: str, number: int):
    return await global_api.fetch_one(country, number)

@app.get("/ml-predict")
def ml_predict(number: int):
    return {"prediction": ml_engine.predict(number)}

@app.get("/prime-check")
def prime_check(number: int):
    return {"prime": rule_engine.check_prime(number)}