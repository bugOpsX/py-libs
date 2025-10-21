"""
Feature: Magic 8-Ball
Description:
A classic toy where users ask a yes/no question and receive a randomized answer.
"""

import random

RESPONSES = [
    # Positive
    "Yes, definitely ✅",
    "It is certain 🌟",
    "Absolutely! 💯",
    "You can count on it 👍",

    # Neutral
    "Ask again later ⏳",
    "Cannot predict now 🤔",
    "Maybe… 🤷‍♂️",
    
    # Negative
    "Nope ❌",
    "Don't count on it 😬",
    "Very doubtful 🙃"
]

def ask_question():
    """Prompt the user for a question and respond with a random answer."""
    question = input("🎱 Ask a yes/no question: ").strip()
    if not question.endswith("?"):
        print("⚠️ That doesn't seem like a question. Make sure it ends with a '?'")
    else:
        answer = random.choice(RESPONSES)
        print(f"\n🪄 Magic 8-Ball says: {answer}\n")

if __name__ == "__main__":
    ask_question()
