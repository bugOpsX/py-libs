# DSA/utils/username_generator.py

"""
Quirky Username / Startup Name Generator 🚀

This module combines random adjectives and nouns (plus optional numbers)
to generate fun usernames like:
    - QuantumPanda42
    - ElectricFalcon
    - SneakyOctopus99

Usage (as a library):
    from DSA.utils.username_generator import generate_username
    print(generate_username())

Usage (CLI):
    python3 DSA/utils/username_generator.py 5
"""

import sys
import random

# Some fun adjectives and nouns (you can expand this list)
ADJECTIVES = [
    "Quantum", "Electric", "Sneaky", "Curious", "Bold", "Whimsical",
    "Mighty", "Cosmic", "Silent", "Swift", "Cheerful", "Savvy",
    "Ethereal", "Zany", "Vivid", "Brave", "Witty", "Luminous"
]

NOUNS = [
    "Panda", "Falcon", "Octopus", "Unicorn", "Phoenix", "Llama",
    "Ninja", "Rocket", "Banana", "Penguin", "Dragon", "Cactus",
    "Pirate", "Chameleon", "Tiger", "Muffin", "Robot", "Galaxy"
]

def generate_username(include_number=True):
    """
    Generate a quirky username by combining a random adjective and noun.
    Optionally append a random number.
    """
    adjective = random.choice(ADJECTIVES)
    noun = random.choice(NOUNS)
    username = adjective + noun

    if include_number:
        username += str(random.randint(1, 99))

    return username


def cli():
    """Command-line interface for generating multiple usernames."""
    count = 1
    if len(sys.argv) == 2:
        try:
            count = int(sys.argv[1])
        except ValueError:
            print("Usage: python3 DSA/utils/username_generator.py [count]")
            return

    print(f"✨ Generating {count} random username(s):\n")
    for _ in range(count):
        print("-", generate_username())


if __name__ == "__main__":
    cli()
