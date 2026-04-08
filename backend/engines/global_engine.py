import asyncio, random

COUNTRY_PROFILES = {
    "us":     {"bias": 0.1,  "label": "US server"},
    "india":  {"bias": 0.15, "label": "India data center"},
    "japan":  {"bias": 0.35, "label": "Japan node"},
    "europe": {"bias": 0.08, "label": "Europe cluster"},
}

async def fetch_one(country: str, n: int) -> dict:
    p = COUNTRY_PROFILES.get(country, COUNTRY_PROFILES["us"])
    await asyncio.sleep(random.uniform(0.2, 1.2))  # fake latency
    unstable = random.random() < p["bias"]
    if unstable:
        return {"country": country, "result": "unstable",
                "log": f"{p['label']} returned unstable response"}
    # Slight random corruption for drama
    vote = (n % 2 == 0) if random.random() > 0.1 else not (n % 2 == 0)
    return {"country": country, "result": "EVEN" if vote else "ODD",
            "log": f"Fetching analysis from {p['label']}..."}

async def fetch_all(n: int) -> dict:
    tasks = [fetch_one(c, n) for c in COUNTRY_PROFILES]
    results = await asyncio.gather(*tasks)
    logs = [r["log"] for r in results]
    votes = [r["result"] for r in results if r["result"] != "unstable"]
    conflicts = len(set(votes)) > 1
    if conflicts:
        logs.append("⚠ Conflict detected between regions. Escalating to multiverse engine.")
    return {"logs": logs, "votes": votes}