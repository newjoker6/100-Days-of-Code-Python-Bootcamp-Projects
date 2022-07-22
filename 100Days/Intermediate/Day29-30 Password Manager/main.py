from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random, pyperclip


chars = ["A", "B", "C", "D", "E", "F", "?", "G", "H", "I", "J", "K", "L", "M",
"N", "O", "P", "&", "Q", "R", "S", "T", "U", "*", "V", "W", "X", "Y", "Z",
 "!", "@", "#", "$", "%", "^", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def generate():
    Password_Entry.delete(0, END)
    password = ""
    length = random.randrange(8, 13)

    for i in range(1, length + 1):
        global chars
        choice = random.choice(chars)
        UL = random.randint(0,1)
        if UL == 0:
            password += choice.upper()
        elif UL == 1:
            password += choice.lower()

    Password_Entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
import json

Data = {}

def save_data(data):
    json.dump(data, open("data.json", "w"), indent=4)

def add_entry(web, user, passw):
    global Data

    if len(Website_Entry.get()) ==0 or len(Password_Entry.get()) == 0:
        messagebox.showerror(title="Error", message="All fields must be filled in.")
    else:
        is_ok = messagebox.askokcancel(title="Save data?", message=f"Are you sure you want to add and save this data?\n\n"
                                                           f"Website: {web.title()}\nUser: {user}\nPassword: {passw}")
        if is_ok:
            web = web.title()
            Data[web] = {}
            Data[web]["User"] = user
            Data[web]["Password"] = passw
            save_data(Data)
            Website_Entry.delete(0,END)
            Password_Entry.delete(0,END)

def load_data(file):
    global Data
    try:
        Data = json.load(open(file))
        # print(Data)
    except:
        pass


# ---------------------------- UI SETUP ------------------------------- #

def Search():
    web = Website_Entry.get().title()
    if web in Data.keys():
        messagebox.showinfo(title=web, message=f"User: {Data[web]['User']}\n"
                                                                   f"Password: {Data[web]['Password']}")
    else:
        messagebox.showerror(title="Error", message=f"No account for {web} website")



root = Tk()
root.title("Password Manager")
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth)
positionDown = int(root.winfo_screenheight()/2 - windowHeight)
root.geometry(f"600x400+{positionRight}+{positionDown}")
root.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
Lock_img = PhotoImage(height=200, width=189, file="logo.png")
canvas.create_image(100, 100, image=Lock_img)
canvas.grid(column=1, row=0)

Website_Label = Label(text="Website:")
Website_Entry = Entry(width=33)
Website_Entry.focus()
Search_Button = Button(text="Search", width=14, command=Search)
Website_Label.grid(column=0, row=1)
Website_Entry.grid(column=1, row=1)
Search_Button.grid(column=2, row=1)

Email_Label = Label(text="Email/Username:", padx=20)
Email_Entry = Entry(width=52)
Email_Entry.insert(0,"")
Email_Label.grid(column=0, row=2)
Email_Entry.grid(column=1, row=2, columnspan=2)

showing = True
def show():
    global showing
    if showing:
        Password_Entry.config(show="*")
        showing=False
    else:
        Password_Entry.config(show="")
        showing=True

Password_Label = Label(text="Password:")
Password_Entry = Entry(width=33)
Show_Button = Button(text="Show", command=show)
Show_Button.grid(column=3, row=3)
Password_Gen_Button = Button(text="Generate Password", command=generate)
Password_Label.grid(column=0, row=3)
Password_Entry.grid(column=1, row=3)
Password_Gen_Button.grid(column=2, row=3)

Add_Button = Button(text="Add", width=44, command= lambda: add_entry(Website_Entry.get(), Email_Entry.get(), Password_Entry.get()))
Add_Button.grid(column=1, row=4, columnspan=2)

load_data("data.json")

root.mainloop()