import emoji

def main():
    print("=== Emoji Fun ===")
    
    # Example 1: Simple emoji
    print(emoji.emojize("Python is fun 🐍"))
    
    # Example 2: Using emoji shortcodes
    print(emoji.emojize("I love coding :laptop:"))
    
    # Example 3: User input
    text = input("Enter a message with emoji shortcodes (e.g., I feel :smile:): ")
    print("Your emoji message:", emoji.emojize(text))
    
    # Example 4: List of emotions
    emotions = {
        "happy": ":smile:",
        "sad": ":cry:",
        "angry": ":angry:",
        "cool": ":sunglasses:",
    }
    
    print("\nAvailable emotions:", ', '.join(emotions.keys()))
    choice = input("How are you feeling today? ").lower()
    
    if choice in emotions:
        print(emoji.emojize(f"You are feeling {emotions[choice]}"))
    else:
        print("Emotion not found. Try again!")

if __name__ == "__main__":
    main()
