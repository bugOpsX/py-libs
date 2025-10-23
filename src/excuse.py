"""
Simple Excuse Generator 🎲

Generates a random, ready-made excuse from a sensible list.

Usage (Library):
    from excuse_generator import get_excuse
    print(get_excuse())

Usage (CLI):
    python3 excuse_generator.py [count]
    count: optional, how many excuses to generate
"""

import random
import sys

# List of full, human-style excuse sentences
EXCUSES = [
    "Sorry, I got stuck in traffic and lost track of time.",
    "I accidentally set my alarm for PM instead of AM.",
    "My internet went down just as I was about to get started.",
    "I wasn’t feeling well this morning.",
    "There was an unexpected power outage in my area.",
    "I had a family emergency I had to deal with.",
    "Honestly, my pet was not cooperating today.",
    "A major software update started right when I needed my computer.",
    "I had to help my neighbor with something urgent.",
    "My phone died while I was on my way.",
    "A surprise guest showed up at my place.",
    "I lost my keys and spent a while looking for them.",
    "I had to attend to a last-minute appointment.",
    "Bad weather delayed everything today.",
    "I received an urgent call that I couldn't ignore.",
]

def get_excuse():
    """Return a random, complete excuse sentence."""
    return random.choice(EXCUSES)

def cli():
    """CLI for the excuse generator."""
    count = 1
    if len(sys.argv) == 2:
        try:
            count = int(sys.argv[1])
        except ValueError:
            print("Usage: python3 excuse_generator.py [count]")
            return
    for _ in range(count):
        print(get_excuse())

if __name__ == "__main__":
    cli()
