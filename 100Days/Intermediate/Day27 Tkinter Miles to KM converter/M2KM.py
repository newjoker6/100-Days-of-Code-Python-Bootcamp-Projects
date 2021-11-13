from tkinter import *





root = Tk()
root.title("Mile to Km Converter")
root.geometry("300x150+1670+300")
root.config(padx=20, pady=20)

Miles_Entry = Entry(justify="center")
Miles_Entry.grid(column=1, row=0)

Miles_Label = Label(text="Miles", font=("Arial", 12, "bold"))
Miles_Label.grid(column=2, row=0)
Miles_Label.config(padx=5, pady=10)

fill_label = Label(text="is equal to", font=("Arial", 12, "bold"))
fill_label.grid(column=0, row=1)
fill_label.config(padx=10)

Result_Label = Label(text="0", font=("Arial", 12, "bold"))
Result_Label.grid(column=1, row=1)
Result_Label.config(padx=20)

Km_Label = Label(text="Km", font=("Arial", 12, "bold"))
Km_Label.grid(column=2, row=1)

def Calculate():
    Miles = Miles_Entry.get()
    Result_Label["text"] = str(float(Miles) * 1.609344)

Calc_Button = Button(text="Calculate", command=Calculate, font=("Arial", 12, "bold"))
Calc_Button.grid(column=1, row=2)


root.mainloop()
