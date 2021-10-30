alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

RUN = True

while RUN:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
    text = input("type your message\n").lower()
    shift = int(input("Type the shift number\n"))

    if shift > len(alphabet):
        shift = shift % 26

    def caesar(direction, plain_text, shift_amount):
        if direction == 'encode':
            encrypted_message = ""
            for char in plain_text:
                if char in alphabet:
                    x = alphabet.index(char)
                    x += shift_amount
                    if x >= len(alphabet):
                        x -= len(alphabet)
                    encrypted_message += alphabet[x]
                else:
                    encrypted_message += char
            print(f"Your encrypted message is {encrypted_message}")

        elif direction == 'decode':
            decrypted_message = ""
            for char in plain_text:
                if char in alphabet:
                    x = alphabet.index(char)
                    x -= shift_amount
                    decrypted_message += alphabet[x]
                else:
                    decrypted_message += char
            print(f"Your decrypted message is {decrypted_message}")


    caesar(direction, text, shift)

    choice = input("Would you like to encrypt/decrypt again?\nyes or no\n")

    if choice == "yes":
        pass
    elif choice == "no":
        RUN = False
        print("Goodbye")