import random, sys

word_list = ["advark", "baboon", "camel"]

lives = 6

guessed_letters = []

chosen_word = word_list[random.randint(0, len(word_list) -1)]
display = []

for letter in chosen_word:
    display.append('_')


print(chosen_word)

while True:
    guess = input("Guess a letter: ").lower()

    if len(guess) > 1:
        print("You can only guess one letter at a time.")

    else:
        if guess in guessed_letters:
            print("You have already guessed " + guess)

        else:
            if not guess in chosen_word:
                guessed_letters.append(guess)
                print(guess + " is not in the word")
                lives -= 1

            for position in range(len(chosen_word)):
                char = chosen_word[position]
                if char == guess:
                    display[position] = char
                    if not guess in guessed_letters:
                        guessed_letters.append(guess)

            print(display)
            print("Lives: " + str(lives))

            if not "_" in display:
                print("Player Wins")
                sys.exit(0)

            if lives == 0:
                print("Player Lost")
                print("Lives: " + str(lives))
                sys.exit(0)