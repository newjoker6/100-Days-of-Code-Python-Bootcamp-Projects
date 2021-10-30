import random, sys



print("Welcome to the number guessing game!")

def number_guesser():
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts: int

    if difficulty == 'easy':
        attempts = 10

    if difficulty == 'hard':
        attempts = 5

    number = random.randint(1, 100)

    while True:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("Make a guess: "))

        if attempts > 0:
            if not guess == number:
                attempts -= 1

                if guess < number:
                    print("Higher")

                elif guess > number:
                    print("Lower")

            else:
                print(f"You Win! I was thinking of {number}")
                break

        if attempts == 0:
            print(f"You lost :( I was thinking of {number}")
            break

playing = True

number_guesser()

while playing:
    choice = input("Would you like to play again? 'y' or 'n'\n").lower()

    if choice == 'y':
        number_guesser()

    else:
        sys.exit(0)