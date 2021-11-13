from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
Title = "Pomodoro"

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    root.after_cancel(timer)
    global reps
    reps = 0
    Timer_Label.config(text="Timer", fg=GREEN)
    Check_Marks.config(text="")
    canvas.itemconfig(timer_text, text=f"00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in [1,3,5,7]:
        Timer_Label.config(text="Work", fg=GREEN)
        countdown(work_sec)
    if reps == 8:
        Timer_Label.config(text="Break", fg=RED)
        countdown(long_break_sec)
    if reps in [2,4,6]:
        Timer_Label.config(text="Break", fg=PINK)
        countdown(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    Minutes = math.floor(count/60)
    Seconds = count %60
    if Seconds > 10:
        canvas.itemconfig(timer_text, text=f"{Minutes}:{Seconds}")
    elif Seconds < 10:
        canvas.itemconfig(timer_text, text=f"{Minutes}:0{Seconds}")
    if count > 0:
        global timer
        timer = root.after(1000, countdown, count-1)
    else:
        root.attributes("-topmost", True)
        root.attributes("-topmost", False)
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        Check_Marks.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title(Title)
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth)
positionDown = int(root.winfo_screenheight()/2 - windowHeight)
root.geometry(f"500x500+{positionRight}+{positionDown}")
root.config(padx=100, pady=50, bg=YELLOW)





canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


Timer_Label = Label(text="Timer", background=YELLOW, fg=GREEN,font=(FONT_NAME, 50, "bold"))
Timer_Label.grid(column=1, row=0)


Check_Marks = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
Check_Marks.grid(column=1, row=4)


Start_Button = Button(text="Start", command=start_timer, font=(FONT_NAME, 9, "bold"))
Start_Button.grid(column=0, row=2)

Reset_Button = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 9, "bold"))
Reset_Button.grid(column=2, row=2)


root.mainloop()