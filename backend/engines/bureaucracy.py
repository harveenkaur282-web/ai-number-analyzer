import asyncio, random

async def process(n: int) -> list:
    logs = ["📋 Filling Form 27B-stroke-6..."]
    await asyncio.sleep(0.3)
    logs.append("🕐 Approval pending... (estimated wait: 3-5 business universes)")
    await asyncio.sleep(0.4)
    if random.random() < 0.4:
        logs.append("❌ Request rejected. Reason: Number too large for department.")
        await asyncio.sleep(0.2)
        logs.append("🔄 Retrying with Form 27B-stroke-7...")
        await asyncio.sleep(0.3)
    logs.append("✅ Bureaucratic clearance obtained. Proceeding.")
    return logs