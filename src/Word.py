# DSA/games/guess_the_word.py

"""
Guess the Word Game

The program randomly selects a word.
The player has to guess the letters of the word one by one.
The game continues until the player guesses the word or runs out of attempts.
"""

import random
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "guess_stats.json")

def load_stats():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"games_won": 0, "games_lost": 0}

def save_stats(stats):
    with open(DATA_FILE, "w") as f:
        json.dump(stats, f, indent=2)

CATEGORIES = {
    "programming": ["python", "function", "variable", "algorithm", "developer"],
    "fruits": ["apple", "banana", "mango", "orange", "grape"],
    "animals": ["tiger", "elephant", "kangaroo", "dolphin", "giraffe"]
}

def guess_the_word():
    hints_used = 0
    MAX_HINTS = 2

    stats = load_stats()
    print("Categories:", ", ".join(CATEGORIES.keys()))

    category = input("Choose a category: ").lower()

    if category not in CATEGORIES:
        print("⚠️ Invalid category! Defaulting to 'programming'.")
        category = "programming"
    words = CATEGORIES[category]

    chosen_word = random.choice(words)
    guessed = ["_"] * len(chosen_word)
    attempts = 7  # Max incorrect guesses
    guessed_letters=[]

    print("🎯 Welcome to Guess the Word!")
    print("The word has", len(chosen_word), "letters.")
    print(" ".join(guessed))

    while attempts > 0 and "_" in guessed:
        letter = input("Guess a letter: ").lower()

        if letter == "hint":
            if hints_used < MAX_HINTS:
                hint_letter = random.choice([c for i, c in enumerate(chosen_word) if guessed[i] == "_"])
                print(f"💡 Hint: The word contains '{hint_letter}'")
                attempts -= 1
                hints_used += 1
                print(f"Attempts left: {attempts}")
            else:
                print("⚠️ No hints left!")
            continue

        if len(letter) != 1 or not letter.isalpha():
            print("⚠️ Enter a valid letter.")
            continue 

        if letter in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue
        guessed_letters.append(letter)
        if letter in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == letter:
                    guessed[i] = letter
            print("✅ Good guess!")
        else:
            attempts -= 1
            print(f"❌ Wrong! Attempts left: {attempts}")

        print(" ".join(guessed))

    if "_" not in guessed:
        print("🎉 Congratulations! You guessed the word:", chosen_word)
        stats["games_won"] += 1
    else:
        print("💀 Game over! The word was:", chosen_word)
        stats["games_lost"] += 1

    print(f"🏆 Stats: {stats['games_won']} wins, {stats['games_lost']} losses")
    save_stats(stats)
    
    if input("Play again? (y/n): ").lower() == "y":
        guess_the_word()

if __name__ == "__main__":
    guess_the_word()