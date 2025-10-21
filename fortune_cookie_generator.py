import random
import time

# --- ANSI COLORS ---
COLORS = {
    "reset": "\033[0m",
    "yellow": "\033[93m",
    "cyan": "\033[96m",
    "green": "\033[92m",
    "magenta": "\033[95m"
}

def type_effect(text, delay=0.04):
    """Print text with typing animation."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def get_fortune(category):
    fortunes = {
        "funny": [
            "If at first you don’t succeed, call it version 1.0.",
            "You will be hungry again in one hour.",
            "Your code works… but only on your machine.",
        ],
        "wise": [
            "Patience is not the ability to wait, but how you act while waiting.",
            "Knowledge is power, but enthusiasm pulls the switch.",
            "You will soon receive an opportunity — don’t let fear stop you.",
        ],
        "sarcastic": [
            "Oh sure, everything will go perfectly. Just like last time.",
            "The road to success is always under construction.",
            "Keep trying. The bug is probably in someone else’s code... right?",
        ]
    }

    if category not in fortunes:
        category = random.choice(list(fortunes.keys()))

    return random.choice(fortunes[category])

if __name__ == "__main__":
    print(COLORS["cyan"] + "🥠 Welcome to the Fortune Cookie Generator!" + COLORS["reset"])
    print("Choose your flavor of fortune:")
    print("1️⃣ Funny\n2️⃣ Wise\n3️⃣ Sarcastic")

    choice = input("Enter 1, 2, or 3: ").strip()
    categories = {"1": "funny", "2": "wise", "3": "sarcastic"}
    category = categories.get(choice, "funny")

    print()
    print(COLORS["yellow"] + "Cracking your fortune cookie..." + COLORS["reset"])
    time.sleep(1.5)
    print()

    fortune = get_fortune(category)
    type_effect(COLORS["magenta"] + fortune + COLORS["reset"])
