import random

def espresso_status():
    if random.random() < 0.3:
        return "System low on caffeine ☕. Performance degraded."
    return "Espresso levels optimal."

def generate(number: int, is_even: bool, is_prime: bool):
    # Special numbers
    special = {
        3: "Third wheel detected 🚲. No one asked for this energy.",
        7: "Lucky number? The algorithm says: maybe. iykyk.",
        11: "Eleven. Stranger Things energy detected.",
        22: "Taylor Swift has entered the chat 🎵 it's giving 22",
        42: "The answer to life, the universe, and everything. Still checking if prime.",
        67: "SIX-SEVEN 👀 iykyk. The streets know.",
        69: "It's giving… we're not going to say it. iykyk.",
        100: "Main character energy ✨ topper detected. Social life: null.",
        404: "Error 404: Social life not found.",
        420: "The system required an espresso break ☕ for this one."
    }

    if number in special:
        base = special[number]
    else:
        templates = [
            f"{number} is being judged by the algorithm.",
            f"⚡ Number {number} just got roasted by AI logic!",
            f"{number} is now famous in the multiverse of numbers.",
            f"Alert 🚨: Number {number} is trending in the meme engine."
        ]
        base = random.choice(templates)

    return base + " | " + espresso_status()


def generate_logs(number: int):
    steps = [
        "🔍 Initializing AI pipeline...",
        f"📥 Received input: {number}",
        "⚙️ Running rule engine...",
        "🎭 Generating meme context...",
        "🌐 Connecting to global servers...",
        "🛰️ Syncing satellite data...",
        "🤖 Consulting neural network...",
        "✅ Analysis complete."
    ]

    # Randomly shuffle some intermediate logs to make them dynamic
    middle = steps[2:-1]
    random.shuffle(middle)

    logs = [steps[0], steps[1]] + middle + [steps[-1]]
    return logs