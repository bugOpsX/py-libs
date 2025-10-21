import random

# Food database
cuisines = ["Italian", "Mexican", "Indian", "Chinese", "Japanese", "Thai", "American", "Mediterranean"]

specific_foods = ["Pizza", "Salad", "Sandwich", "Burger", "Pasta", "Tacos", "Sushi", "Curry", 
                  "Stir Fry", "Soup", "Ramen", "Burrito", "Wrap", "Grilled Chicken", "Fried Rice"]

meals_by_cuisine = {
    "Italian": ["Pizza", "Pasta", "Lasagna", "Risotto", "Ravioli"],
    "Mexican": ["Tacos", "Burrito", "Quesadilla", "Enchiladas", "Nachos"],
    "Indian": ["Curry", "Biryani", "Tandoori Chicken", "Samosas", "Naan with Dal"],
    "Chinese": ["Fried Rice", "Chow Mein", "Sweet and Sour Chicken", "Dumplings", "Kung Pao"],
    "Japanese": ["Sushi", "Ramen", "Teriyaki", "Tempura", "Udon"],
    "Thai": ["Pad Thai", "Green Curry", "Tom Yum Soup", "Spring Rolls", "Massaman Curry"],
    "American": ["Burger", "Hot Dog", "BBQ Ribs", "Mac and Cheese", "Buffalo Wings"],
    "Mediterranean": ["Falafel", "Hummus Wrap", "Greek Salad", "Kebab", "Gyros"]
}

def print_header():
    print("\n" + "=" * 50)
    print("🍽️  WHAT TO EAT GENERATOR 🍽️")
    print("=" * 50)

def suggest_cuisine():
    cuisine = random.choice(cuisines)
    print(f"\n✨ Suggestion: Try {cuisine} food today!")
    

    if cuisine in meals_by_cuisine:
        specific = random.choice(meals_by_cuisine[cuisine])
        print(f"   How about: {specific}?")

def suggest_specific_food():
    food = random.choice(specific_foods)
    print(f"\n✨ Suggestion: Go for {food}!")

def suggest_with_cuisine_detail():
    cuisine = random.choice(cuisines)
    if cuisine in meals_by_cuisine:
        dish = random.choice(meals_by_cuisine[cuisine])
        print(f"\n✨ Suggestion: {dish} ({cuisine} cuisine)")
    else:
        print(f"\n✨ Suggestion: Try {cuisine} food today!")

def custom_suggestion():
    print("\n📝 Enter your food options (separated by commas):")
    user_input = input("Example: Pizza, Salad, Pasta\n> ")
    
    if user_input.strip():
        options = [option.strip() for option in user_input.split(",")]
        if options:
            choice = random.choice(options)
            print(f"\n✨ Suggestion: Go for {choice}!")
        else:
            print("No valid options entered!")
    else:
        print("No options entered!")

def display_menu():
    print("\nWhat would you like me to help you choose?")
    print("1. Suggest a cuisine type")
    print("2. Suggest a specific food")
    print("3. Suggest a dish with cuisine")
    print("4. Choose from my own list")
    print("5. Exit")
    print()

def main():
    print_header()
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == "1":
                suggest_cuisine()
            elif choice == "2":
                suggest_specific_food()
            elif choice == "3":
                suggest_with_cuisine_detail()
            elif choice == "4":
                custom_suggestion()
            elif choice == "5":
                print("\n👋 Happy eating! Goodbye!")
                break
            else:
                print("\n❌ Invalid choice! Please enter 1-5.")
                

            if choice in ["1", "2", "3", "4"]:
                again = input("\nWant another suggestion? (yes/no): ").lower()
                if again not in ["yes", "y"]:
                    print("\n👋 Happy eating! Goodbye!")
                    break
                    
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()