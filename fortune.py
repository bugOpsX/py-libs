"""
Feature: Random Fortune Messages
Description:
Prints a random “fortune” message each time the script is run.
Messages can be serious, funny, or sarcastic.
"""

import random

FORTUNES = [
    # Serious
    "💡 Stay focused today; your efforts will pay off.",
    "🌱 Personal growth comes from challenges, not comfort.",
    "📈 Small steps consistently lead to big results.",
    
    # Funny
    "😂 Today, your coffee will be stronger than your Wi-Fi signal.",
    "🐢 Slow and steady wins the race, but the hare took a nap.",
    "🍕 Happiness is a warm slice of pizza.",
    
    # Sarcastic
    "🙃 Sure, ignore the instructions… what could go wrong?",
    "😏 Your brilliance is only rivaled by your procrastination.",
    "🤦‍♂️ Another day, another questionable decision."
]

def show_fortune():
    """Pick and display a random fortune."""
    fortune = random.choice(FORTUNES)
    print(f"\n🎴 Your Fortune: {fortune}\n")

if __name__ == "__main__":
    show_fortune()
