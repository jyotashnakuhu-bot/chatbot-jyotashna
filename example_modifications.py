# Example Modifications for Your Chatbot
# This file shows you how to add new features to your chatbot

def rock_paper_scissors():
    """A simple rock, paper, scissors game"""
    print("\n🪨📄✂️ Let's play Rock, Paper, Scissors!")
    print("1. Rock 🪨")
    print("2. Paper 📄")
    print("3. Scissors ✂️")
    
    choice = input("What do you choose? (1-3): ")
    
    # Convert choice to text
    choices = {"1": "Rock", "2": "Paper", "3": "Scissors"}
    user_choice = choices.get(choice, "Rock")
    
    # Computer makes a random choice
    import random
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    print(f"You chose: {user_choice}")
    print(f"I chose: {computer_choice}")
    
    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie! 🤝")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        print("You win! 🎉")
    else:
        print("I win! 😄")

def math_quiz():
    """A simple math quiz"""
    print("\n🧮 Let's do some math!")
    
    import random
    score = 0
    questions = 3
    
    for i in range(questions):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 + num2
        
        print(f"\nQuestion {i+1}: What is {num1} + {num2}?")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == answer:
                print("Correct! ✅")
                score += 1
            else:
                print(f"Wrong! The answer was {answer} ❌")
        except ValueError:
            print("Please enter a number!")
    
    print(f"\nYou got {score} out of {questions} correct!")
    if score == questions:
        print("Perfect score! You're a math genius! 🧠")
    elif score >= questions/2:
        print("Good job! Keep practicing! 👍")
    else:
        print("Keep practicing, you'll get better! 💪")

def compliment_generator():
    """Generate random compliments"""
    compliments = [
        "You're awesome! 🌟",
        "You have a great smile! 😊",
        "You're really smart! 🧠",
        "You're kind and caring! ❤️",
        "You're creative and imaginative! 🎨",
        "You're brave and strong! 💪",
        "You make the world a better place! 🌍",
        "You're a great friend! 🤝",
        "You're talented and amazing! ⭐",
        "You're doing great things! 🎉"
    ]
    
    import random
    print("\n💝 Here's a compliment for you:")
    print(random.choice(compliments))

def story_generator():
    """Generate a simple story"""
    print("\n📖 Let me tell you a story!")
    
    # Get some details from the user
    name = input("What's the main character's name? ")
    animal = input("What's their favorite animal? ")
    color = input("What's their favorite color? ")
    
    # Create a simple story
    story = f"""
Once upon a time, there was a brave young person named {name}.
{name} loved {animal}s more than anything in the world.
One day, {name} found a magical {color} {animal} in the forest.
The {animal} could talk and became {name}'s best friend!
Together, they went on amazing adventures and learned that friendship
is the most magical thing of all.

The End! 🎭
"""
    print(story)

# Example of how to add these to your main menu:
def show_enhanced_menu():
    """Show an enhanced menu with new features"""
    print("\n" + "="*50)
    print("🤖 ENHANCED CHATBOT MENU 🤖")
    print("="*50)
    print("1. Tell me a joke 😄")
    print("2. Play a number game 🎮")
    print("3. Ask how I'm feeling 😊")
    print("4. Learn about programming 💻")
    print("5. Play Rock, Paper, Scissors 🪨📄✂️")
    print("6. Take a math quiz 🧮")
    print("7. Get a compliment 💝")
    print("8. Generate a story 📖")
    print("9. Exit 👋")
    print("="*50)

# Example of how to modify your main function to include new features:
def enhanced_main():
    """Enhanced main function with new features"""
    print("🚀 Starting your enhanced learning chatbot...")
    import time
    time.sleep(1)
    
    # Greet the user (you can copy the greet_user function from simple_chatbot.py)
    print("🤖 Hi! I'm your enhanced learning chatbot!")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}! 👋")
    
    # Main conversation loop
    while True:
        show_enhanced_menu()
        choice = input(f"\n{name}, what would you like to do? (1-9): ")
        
        if choice == "1":
            print("\n" + "Why don't scientists trust atoms? Because they make up everything! 😄")
        elif choice == "2":
            print("\n🎮 Number game feature would go here!")
        elif choice == "3":
            print("\n😊 Mood feature would go here!")
        elif choice == "4":
            print("\n💻 Programming lesson would go here!")
        elif choice == "5":
            rock_paper_scissors()
        elif choice == "6":
            math_quiz()
        elif choice == "7":
            compliment_generator()
        elif choice == "8":
            story_generator()
        elif choice == "9":
            print(f"\n👋 Goodbye, {name}! Thanks for chatting with me!")
            break
        else:
            print("I didn't understand that. Please choose 1-9.")
        
        input("\nPress Enter to continue...")

# Uncomment the line below to test the enhanced chatbot:
# enhanced_main()
