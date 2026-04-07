import random, asyncio

NODES = {
    "US": {"delay": 0.1, "bias": "stable"},
    "India": {"delay": 0.2, "bias": "stable"},
    "Japan": {"delay": 0.3, "bias": "unstable"},
    "Europe": {"delay": 0.15, "bias": "stable"},
}

def fetch_all(n):
    logs = []
    results = {}
    for country, cfg in NODES.items():
        logs.append(f"Fetching analysis from {country} data center...")
        if cfg["bias"] == "unstable" or random.random() < 0.15:
            logs.append(f"{country} node returned: UNSTABLE RESPONSE ⚠️")
            results[country] = "UNSTABLE"
        else:
            verdict = "EVEN" if n % 2 == 0 else "ODD"
            # 10% chance of a country just being wrong
            if random.random() < 0.10:
                verdict = "ODD" if verdict == "EVEN" else "EVEN"
                logs.append(f"Conflict detected: {country} disagrees with consensus!")
            results[country] = verdict
    return results, logs