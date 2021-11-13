import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())
print(data.iterrows())

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    username = input("What is your name?\n")

    try:
        name_list = [phonetic_dict[letter.upper()] for letter in username]

    except KeyError:
        print("Only letters in the alphabet are permitted")
        generate_phonetic()

    else:
        print(name_list)


generate_phonetic()
