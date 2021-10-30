import sys

direction = input("left or right?\n")

if direction == "right":
    print("Game Over")


elif direction == "left":
    decision = input("swim or wait?\n")

    if decision == "swim":
        print("Game Over")


    elif decision == "wait":
        door = input("Select a door, Red, Blue or Yellow\n")

        if door == "Red":
            print("Game Over")


        elif door == "Blue":
            print("Game Over")


        elif door == "Yellow":
            print("Winner is you!")



