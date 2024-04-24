import random

user_action = input("Enter a choice (rock, paper, scissor): ")
possible_actions = ["rock", "paper", "scissor"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n") #f hm isliye use krte h ta k yeh user k liye easy ho jaye variables ko add krna ya , lgana ya curly braces ko use krna etc.

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win....HAPPY")
    else:
        print("Paper covers rock! You lose....SAD")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win....HAPPY")
    else:
        print("Scissors cuts paper! You lose....SAD")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win...HAPPY")
    else:
        print("Rock smashes scissors! You lose...SAD")