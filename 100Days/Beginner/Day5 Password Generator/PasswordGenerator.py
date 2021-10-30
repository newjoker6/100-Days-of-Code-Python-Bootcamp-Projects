import random


chars = ["A", "B", "C", "D", "E", "F", "?", "G", "H", "I", "J", "K", "L", "M",
"N", "O", "P", "&", "Q", "R", "S", "T", "U", "*", "V", "W", "X", "Y", "Z",
 "!", "@", "#", "$", "%", "^", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


length = int(input("How many characters long?\n"))
password = ""


for i in range(1, length + 1):
    choice = random.choice(chars)
    UL = random.randint(0,1)
    if UL == 0:
        password += choice.upper()
    elif UL == 1:
        password += choice.lower()

print(password)