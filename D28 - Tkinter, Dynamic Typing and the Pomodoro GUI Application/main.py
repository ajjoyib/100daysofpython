from tkinter import *
from tkinter import ttk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
CHECKMARK = "✓"
reps = 0
timer = None



# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec =  WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", foreground=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", foreground=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", foreground=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += CHECKMARK
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")

frm = Frame(window, padx=100, pady=50, bg=YELLOW)
frm.grid()

# Timer Title
title = ttk.Label(frm, text="Timer", font=(FONT_NAME, 34, "bold"), background=YELLOW, foreground=GREEN)
title.grid(column=2, row=1)

# Tomato Image
canvas = Canvas(frm, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=2, row=2)

# Start & Reset Buttons
start = ttk.Button(frm, text="Start", command=start_timer)
reset = ttk.Button(frm, text="Reset", command=reset_timer)
start.grid(column=1, row=3)
reset.grid(column=3, row=3)

# Check Mark
checkmark = ttk.Label(frm, text="", background=YELLOW, foreground=GREEN)
checkmark.grid(column=2, row=4)







window.mainloop()
