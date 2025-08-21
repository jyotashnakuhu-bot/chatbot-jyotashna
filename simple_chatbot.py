# Simple Chatbot for Learning Python!
# This is a basic chatbot that you can understand and modify

import random
import time

def greet_user():
    """Say hello to the user and get their name"""
    print("🤖 Hi! I'm your friendly learning chatbot!")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}! 👋")
    return name

def get_user_mood():
    """Ask how the user is feeling"""
    print("\nHow are you feeling today?")
    print("1. Happy 😊")
    print("2. Sad 😢")
    print("3. Excited 🎉")
    print("4. Tired 😴")
    print("5. Just okay 🤷")
    
    choice = input("Enter a number (1-5): ")
    
    responses = {
        "1": "That's wonderful! I'm happy you're happy! 😊",
        "2": "I'm sorry you're feeling sad. Maybe I can cheer you up! 🌟",
        "3": "Wow! What are you excited about? That's awesome! 🎉",
        "4": "Being tired is totally normal. Maybe take a little break? 😴",
        "5": "That's okay! Sometimes 'just okay' is perfectly fine! 🤷"
    }
    
    return responses.get(choice, "I'm not sure what that means, but I hope you're doing well!")

def play_number_game():
    """Play a simple number guessing game"""
    print("\n🎮 Let's play a number guessing game!")
    print("I'm thinking of a number between 1 and 10...")
    
    secret_number = random.randint(1, 10)
    attempts = 0
    
    while attempts < 3:
        try:
            guess = int(input("What's your guess? "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try a higher number! ⬆️")
            elif guess > secret_number:
                print("Too high! Try a lower number! ⬇️")
            else:
                print(f"🎉 Congratulations! You got it in {attempts} tries!")
                return True
                
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"Game over! The number was {secret_number}. Better luck next time!")
    return False

def tell_joke():
    """Tell a random joke"""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything! 😄",
        "What do you call a fake noodle? An impasta! 🍝",
        "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
        "What do you call a bear with no teeth? A gummy bear! 🐻",
        "Why don't eggs tell jokes? They'd crack each other up! 🥚"
    ]
    return random.choice(jokes)

def show_menu():
    """Show the main menu of options"""
    print("\n" + "="*50)
    print("🤖 CHATBOT MENU 🤖")
    print("="*50)
    print("1. Tell me a joke 😄")
    print("2. Play a number game 🎮")
    print("3. Ask how I'm feeling 😊")
    print("4. Learn about programming 💻")
    print("5. Exit 👋")
    print("="*50)

def teach_programming():
    """Teach some basic programming concepts"""
    print("\n💻 Let's learn about programming!")
    print("Programming is like giving instructions to a computer.")
    print("Just like how you follow steps to make a sandwich,")
    print("computers follow steps (called 'code') to do things!")
    
    print("\nHere are some cool programming concepts:")
    print("• Variables: Like boxes that store information")
    print("• Functions: Like recipes that do specific tasks")
    print("• Loops: Like repeating something over and over")
    print("• Conditions: Like making decisions (if this, then that)")
    
    print("\nIn this chatbot, we used:")
    print("• Variables: to store your name and choices")
    print("• Functions: like greet_user() and play_number_game()")
    print("• Loops: in the number guessing game")
    print("• Conditions: to respond differently based on your mood")

def main():
    """The main function that runs the chatbot"""
    print("🚀 Starting your learning chatbot...")
    time.sleep(1)
    
    # Greet the user
    user_name = greet_user()
    
    # Ask about their mood
    mood_response = get_user_mood()
    print(mood_response)
    
    # Main conversation loop
    while True:
        show_menu()
        choice = input(f"\n{user_name}, what would you like to do? (1-5): ")
        
        if choice == "1":
            print("\n" + tell_joke())
        elif choice == "2":
            play_number_game()
        elif choice == "3":
            mood_response = get_user_mood()
            print(mood_response)
        elif choice == "4":
            teach_programming()
        elif choice == "5":
            print(f"\n👋 Goodbye, {user_name}! Thanks for chatting with me!")
            print("Come back soon to learn more about programming! 💻")
            break
        else:
            print("I didn't understand that. Please choose 1, 2, 3, 4, or 5.")
        
        input("\nPress Enter to continue...")

# This is where the program starts!
if __name__ == "__main__":
    main()
