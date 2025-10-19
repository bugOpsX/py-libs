# simple_dice_roller.py
import random  # Import the random module to generate dice rolls

print("🎲 Dice Roller 🎲")  # Print a title for the program

# Ask the user how many times they want to roll the dice
rolls = int(input("How many dice rolls? "))

# Loop over the number of rolls and print the result each time
for i in range(rolls):
    print(f"Roll {i+1}: {random.randint(1,6)}")
