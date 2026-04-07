import random

def espresso_status():
    if random.random() < 0.3:
        return "System low on caffeine ☕. Performance degraded."
    return "Espresso levels optimal."

def generate(n):
    if n == 3:
        base = "Third wheel detected 💔"
    elif n == 67:
        base = "SIX-SEVEN 👀 iykyk"
    elif n == 404:
        base = "Error 404: Motivation not found."
    elif n == 22:
        base = "Taylor Swift mode activated 🎵"
    elif n == 420:
        base = "System paused for... reasons 🌿"
    else:
        base = f"{n} is being judged by the algorithm."

    return base + " | " + espresso_status()