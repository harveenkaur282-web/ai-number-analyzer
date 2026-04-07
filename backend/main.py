from fastapi import FastAPI
from backend.engines import rule_engine, meme_engine  

app = FastAPI()

@app.get("/analyze/{number}")
def analyze(number: int):
    logs = []

    logs.append("🔍 Initializing AI pipeline...")
    logs.append(f"📥 Received input: {number}")

    logs.append("⚙️ Running rule engine...")
    result = rule_engine.analyze(number)

    logs.append("🎭 Generating meme context...")
    meme = meme_engine.generate(number)

    logs.append("🌐 Connecting to global servers...")
    logs.append("🛰️ Syncing satellite data...")
    logs.append("🤖 Consulting neural network...")

    logs.append("✅ Analysis complete.")

    return {
        "number": number,
        "even": result["even"],
        "prime": result["prime"],
        "meme": meme,
        "logs": logs
    }