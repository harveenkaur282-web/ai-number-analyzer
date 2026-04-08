def decide(ml_pred, is_even, votes):
    logs = ["🌌 Entering multiverse decision layer..."]

    even_votes = votes.count("EVEN")
    odd_votes = votes.count("ODD")

    if even_votes > odd_votes:
        verdict = "EVEN"
    else:
        verdict = "ODD"

    confidence = abs(even_votes - odd_votes) / max(len(votes), 1)

    logs.append(f"🧠 Multiverse consensus: {verdict}")

    return {
        "verdict": verdict,
        "confidence": confidence,
        "logs": logs,
        "status": "stable" if confidence > 0.5 else "uncertain"
    }