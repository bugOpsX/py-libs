#word game where you create a story 

while True:
    print("Lets Make a Story By Your Choice!")
    print("Sounds Exiting Right!!")

    name = input("Enter Character's Name: ")
    place = input("Enter a place: ")
    pet = input("Enter the type of pet: ")
    food = input("Enter a snacks: ")
    expression = input("Enter an expression of Character (smiled, frowned, laughed): ")
    verb=input("Enter a verb (running, jumping, dancing): ")
    adj=input("Enter an adjective (lazy, smart, funny, etc.): ")

    print("Your Story".center(135,"-"))
    print(f"My name is {name} a very {adj} person.\nBut Surprisingly today I went to {place} where people like was never comes.\nBeside that, there was a park, and people took their pets for walk.\nA person came near me and he has a {pet} with him.\nI was sitting and eating {food}, that {pet} was looking at me as he wanted to snatch my World's Last Bite.\nBut as i told you I am lazy, I ignored him and {expression} at him.\nAfter that the {pet} starts {verb}.")
    
    choice=input("Do you want to create another story(yes/no): ").lower()

    if choice!="yes":
        print("Thank you for playing.Good Bye!!")
        break
        
