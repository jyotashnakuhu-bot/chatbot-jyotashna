# Rock Paper Scissors Game! 🪨📄✂️
# A fun game to play against the computer

import random
import time

def show_welcome():
    """Welcome the user to the game"""
    print("🎮 Welcome to Rock Paper Scissors! 🎮")
    print("=" * 40)
    print("🪨 Rock beats Scissors")
    print("📄 Paper beats Rock") 
    print("✂️ Scissors beats Paper")
    print("=" * 40)

def get_user_choice():
    """Get the user's choice with validation"""
    while True:
        print("\nWhat's your choice?")
        print("1. 🪨 Rock")
        print("2. 📄 Paper") 
        print("3. ✂️ Scissors")
        
        choice = input("Enter 1, 2, or 3: ").strip()
        
        if choice == "1":
            return "rock"
        elif choice == "2":
            return "paper"
        elif choice == "3":
            return "scissors"
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

def get_computer_choice():
    """Get a random choice for the computer"""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine who wins the round"""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

def display_choices(user_choice, computer_choice):
    """Display both choices with emojis"""
    emoji_map = {
        "rock": "🪨",
        "paper": "📄", 
        "scissors": "✂️"
    }
    
    print(f"\nYou chose: {emoji_map[user_choice]} {user_choice.title()}")
    print(f"Computer chose: {emoji_map[computer_choice]} {computer_choice.title()}")

def display_result(result, user_choice, computer_choice):
    """Display the result of the round"""
    if result == "tie":
        print("\n🤝 It's a tie! Try again!")
    elif result == "user":
        print(f"\n🎉 You win! {user_choice.title()} beats {computer_choice.title()}!")
    else:
        print(f"\n😔 You lose! {computer_choice.title()} beats {user_choice.title()}!")

def play_round():
    """Play one round of rock paper scissors"""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    # Add some suspense
    print("\nRock...")
    time.sleep(0.5)
    print("Paper...")
    time.sleep(0.5)
    print("Scissors...")
    time.sleep(0.5)
    print("Shoot! 🎯")
    
    display_choices(user_choice, computer_choice)
    result = determine_winner(user_choice, computer_choice)
    display_result(result, user_choice, computer_choice)
    
    return result

def show_score(user_wins, computer_wins, ties):
    """Display the current score"""
    print(f"\n📊 Current Score:")
    print(f"   You: {user_wins} wins")
    print(f"   Computer: {computer_wins} wins") 
    print(f"   Ties: {ties}")

def play_game():
    """Main game function"""
    show_welcome()
    
    user_wins = 0
    computer_wins = 0
    ties = 0
    
    while True:
        result = play_round()
        
        if result == "user":
            user_wins += 1
        elif result == "computer":
            computer_wins += 1
        else:
            ties += 1
            
        show_score(user_wins, computer_wins, ties)
        
        # Ask if they want to play again
        while True:
            play_again = input("\nDo you want to play again? (y/n): ").lower().strip()
            if play_again in ["y", "yes"]:
                break
            elif play_again in ["n", "no"]:
                print(f"\n🎮 Thanks for playing!")
                print(f"Final Score - You: {user_wins}, Computer: {computer_wins}, Ties: {ties}")
                if user_wins > computer_wins:
                    print("🏆 You're the overall winner! Great job!")
                elif computer_wins > user_wins:
                    print("🤖 The computer won this time. Better luck next time!")
                else:
                    print("🤝 It's a tie overall! You're evenly matched!")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")

def main():
    """Start the game"""
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for playing! Goodbye!")
    except Exception as e:
        print(f"\n❌ Something went wrong: {e}")
        print("Please try running the game again.")

# This is where the program starts!
if __name__ == "__main__":
    main()
