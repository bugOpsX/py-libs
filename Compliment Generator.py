# DSA/utils/compliment_generator.py

"""
Wholesome Compliment & Motivation Generator 🌼

This script generates random compliments, motivational quotes,
or funny praises. Think of it as the opposite of a roast generator. 🫶

Usage (as library):
    from DSA.utils.compliment_generator import get_compliment
    print(get_compliment())

Usage (CLI):
    python3 DSA/utils/compliment_generator.py [count]
"""

import random
import sys

# Compliments 🫶
COMPLIMENTS = [
    "You're like a ray of sunshine on a cloudy day ☀️",
    "You make the world a better place just by being you ✨",
    "You're not just smart — you're code-smart 🧠💻",
    "You're the human equivalent of a perfectly written function 👌",
    "You bring positive energy wherever you go 🌻",
    "You're basically the main character 🦸",
    "You have the best kind of weird — the awesome kind 😎",
    "You're proof that kindness is contagious 💖",
    "Your presence improves the vibe of any room you're in 🌈",
    "You're crushing it more than a `while True` loop 🫡",
]

# Motivational one-liners 🚀
MOTIVATIONS = [
    "Keep going — future you will thank you 🔥",
    "Even small steps move you forward 🪴",
    "Progress, not perfection ✨",
    "You’ve got this. Like, actually. 💪",
    "Today is the perfect day to win at something 🏆",
    "The bug isn’t bigger than you — you are the debugger 🧠",
    "You're doing better than you think 🌟",
    "Consistency beats intensity. Keep at it 👣",
    "Your potential is loading... and it’s at 99% ⚡",
    "If you can dream it, you can deploy it 🚀",
]

# Funny praises 😆
PRAISES = [
    "You're the semicolon that completes my statement 😉",
    "If compliments were commits, you'd be a merge with no conflicts 🔥",
    "You’re like an API that always responds with 200 OK ✅",
    "Your energy is more powerful than a double espresso ☕",
    "You're rarer than a bug-free production push 👑",
    "If charisma was code, you'd be open source perfection 😎",
    "You're the human version of autocomplete — always making things better 🔥",
    "You’d be a legendary Pokémon if this were an RPG 🐉",
    "You're like WiFi — when you're around, everything connects 💫",
    "You have main-character energy, and the plot twist loves you 📽️",
]


def get_compliment(category=None):
    """
    Return a random compliment, motivation, or praise.
    Optional category: "compliment", "motivation", "praise".
    """
    if category == "compliment":
        return random.choice(COMPLIMENTS)
    elif category == "motivation":
        return random.choice(MOTIVATIONS)
    elif category == "praise":
        return random.choice(PRAISES)
    else:
        all_lines = COMPLIMENTS + MOTIVATIONS + PRAISES
        return random.choice(all_lines)


def cli():
    """Command-line interface for generating compliments."""
    count = 1
    if len(sys.argv) == 2:
        try:
            count = int(sys.argv[1])
        except ValueError:
            print("Usage: python3 DSA/utils/compliment_generator.py [count]")
            return

    for _ in range(count):
        print(get_compliment())


if __name__ == "__main__":
    cli()
