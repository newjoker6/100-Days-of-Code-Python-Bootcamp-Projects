from tkinter import *
import pandas
import random

DataCSV = pandas.read_csv("data/RussianEnglish1000.csv")
Words = DataCSV.to_dict()
idx = None
timer = None


def select_word():
    global idx, timer, flip_timer
    root.after_cancel(flip_timer)
    idx = random.randint(0, len(Words["Russian"]))
    word1 = Words["Russian"][idx]
    canvas.itemconfig(card_title, text="Russian", fill="black")
    canvas.itemconfig(card_word, text=word1, fill="black")
    canvas.itemconfig(card_image, image=flashcard_img_front)

    flip_timer = root.after(3000, func=flip_card)

def flip_card():
    global timer
    word2 = Words["English"][idx]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word2, fill="white")
    canvas.itemconfig(card_image, image=flashcard_img_back)


BACKGROUND_COLOR = "#B1DDC6"

root = Tk()
root.title("Russian Flashcards")
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth)
positionDown = int(root.winfo_screenheight()/2 - windowHeight)
root.geometry(f"900x700+{positionRight}+{positionDown}")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = root.after(5000, func=flip_card)


flashcard_img_front = PhotoImage(width=800, height=526, file="images/card_front.png")
flashcard_img_back = PhotoImage(width=800, height=526, file="images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=flashcard_img_front)
card_title = canvas.create_text(400, 150, text="Russian", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

no_button_img = PhotoImage(file="images/wrong.png" )
no_button = Button(image=no_button_img, borderwidth=0, bg=BACKGROUND_COLOR, command=select_word)
no_button.grid(column=0, row=1)

yes_button_img = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_button_img, borderwidth=0, bg=BACKGROUND_COLOR, command=select_word)
yes_button.grid(column=1, row=1)

select_word()





root.mainloop()