# DSA/games/guess_the_word.py

"""
Guess the Word Game

The program randomly selects a word.
The player has to guess the letters of the word one by one.
The game continues until the player guesses the word or runs out of attempts.
"""

import random

def guess_the_word():
    words = ["python", "function", "variable", "algorithm", "developer"]
    chosen_word = random.choice(words)
    guessed = ["_"] * len(chosen_word)
    attempts = 7  # Max incorrect guesses

    print("🎯 Welcome to Guess the Word!")
    print("The word has", len(chosen_word), "letters.")
    print(" ".join(guessed))

    while attempts > 0 and "_" in guessed:
        letter = input("Guess a letter: ").lower()

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
    else:
        print("💀 Game over! The word was:", chosen_word)

if __name__ == "__main__":
    guess_the_word()

