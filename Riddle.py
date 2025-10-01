# DSA/utils/riddle_generator.py

"""
Random Riddle Generator 🧩

This module displays random riddles from a JSON dataset.
Optionally, it can show the answer immediately or hide it for guessing.

Usage (Library):
    from DSA.utils.riddle_generator import get_random_riddle
    riddle = get_random_riddle()
    print(riddle['question'])
    print("Answer:", riddle['answer'])

Usage (CLI):
    python3 DSA/utils/riddle_generator.py [show_answer]
    show_answer: optional, "yes" to display the answer immediately
"""

import json
import random
import sys
import os

# Path to the JSON dataset
DATA_FILE = os.path.join(os.path.dirname(__file__), "riddles.json")

# Load riddles from JSON
def load_riddles():
    if not os.path.exists(DATA_FILE):
        # Create sample riddles if file doesn't exist
        sample_riddles = [
            {"question": "What has keys but can't open locks?", "answer": "A piano"},
            {"question": "What has hands but can't clap?", "answer": "A clock"},
            {"question": "What has to be broken before you can use it?", "answer": "An egg"},
            {"question": "I speak without a mouth and hear without ears. What am I?", "answer": "An echo"},
            {"question": "What gets wetter as it dries?", "answer": "A towel"}
        ]
        with open(DATA_FILE, "w") as f:
            json.dump(sample_riddles, f, indent=2)
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def get_random_riddle():
    """Return a random riddle as a dictionary with 'question' and 'answer'."""
    riddles = load_riddles()
    return random.choice(riddles)


def cli():
    """Command-line interface for random riddle generator."""
    show_answer = False
    if len(sys.argv) == 2 and sys.argv[1].lower() in ["yes", "true", "1"]:
        show_answer = True

    riddle = get_random_riddle()
    print("🧩 Riddle:")
    print(riddle["question"])
    if show_answer:
        print("\n💡 Answer:")
        print(riddle["answer"])
    else:
        input("\nPress Enter to reveal the answer...")
        print("💡 Answer:")
        print(riddle["answer"])


if __name__ == "__main__":
    cli()
