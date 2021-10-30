import GameData as GD
import random, os

data = GD.data
clear = lambda: os.system('cls')

score: int
score = 0

A = data[random.randint(0, len(data)-1)]
B = data[random.randint(0, len(data)-1)]


print("Welcome to Higher Lower!")
print("Who has more followers on instagram?\n")


while True:
    while B["name"] == A["name"]:
        B = data[random.randint(0, len(data) - 1)]
    print(f"A: {A['name']}, a {A['description']} from {A['country']}")
    print("or")
    print(f"B: {B['name']}, a {B['description']} from {B['country']}\n")

    guess = input("Who has more? A or B: ").upper()

    if guess == "A":
        if A["follower_count"] < B["follower_count"]:
            clear()
            print(f"You Lost, final score of {score}")
            break

        elif A["follower_count"] > B["follower_count"]:
            clear()
            print(f"Correct, {A['name']} has {A['follower_count']} million followers.\n")
            score += 1
            A = B
            B = data[random.randint(0, len(data))]

    elif guess == "B":
        if B["follower_count"] < A["follower_count"]:
            clear()
            print(f"You Lost, final score of {score}")
            break

        elif B["follower_count"] > A["follower_count"]:
            clear()
            print(f"Correct, {B['name']} has {B['follower_count']} million followers.\n")
            score += 1
            A = B
            B = data[random.randint(0, len(data)-1)]