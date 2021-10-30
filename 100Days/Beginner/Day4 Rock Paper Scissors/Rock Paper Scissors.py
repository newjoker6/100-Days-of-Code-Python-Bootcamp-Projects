import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You Win")

elif computer_choice > user_choice:
    print("You Lose")

elif user_choice >= 3 or user_choice < 0:
    print("Disqualified for invalid number!")

elif user_choice > computer_choice:
    print("You Win")

elif user_choice == computer_choice:
    print("Draw")

else:
    print("You did not enter a number")