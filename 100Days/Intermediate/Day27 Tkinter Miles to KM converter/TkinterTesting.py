import tkinter

window = tkinter.Tk()


window.title("Tkinter Project")
window.minsize(200, 300)
window.geometry("500x600+1670+360")




#Labels
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)

my_label["text"] = "new_text"
my_label.config(padx=10, pady=10)

#Entry

input = tkinter.Entry(width=25)
# input.pack(padx=20, pady=10)
input.grid(column=3, row=2)


#Buttons

def button_clicked():
    my_label["text"] = input.get()


my_button = tkinter.Button(text="My button", command= button_clicked)
# my_button.pack()
my_button.grid(column=1, row=1)
my_button.config(padx=10, pady=10)

new_button = tkinter.Button(text="New button")
new_button.grid(column=2, row=0)
new_button.config(padx=10, pady=10)





window.mainloop()
