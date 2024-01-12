from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
Reps = 5
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(width=200, height=225, bg=YELLOW, padx=100, pady=50)
window.title("Pomodoro")

import math


def reset_timer():
    window.after_cancel(timer)
    status.config(text="Timer", fg="Green")
    canvas.itemconfig(timer_count, text="00:00")
    check_mark.config(text="")
    global Reps
    Reps = 0


def start_timer():
    global Reps
    Reps += 1

    work_seconds = WORK_MIN * 60
    short_rest_seconds = SHORT_BREAK_MIN * 60
    long_rest_seconds = LONG_BREAK_MIN * 60

    if Reps % 8 == 0:
        countdown_timer(long_rest_seconds)
        status.config(text="Long Break", fg=RED, font=(FONT_NAME, 35, "bold"))
    elif Reps % 2 == 0:
        countdown_timer(short_rest_seconds)
        status.config(text="Short Break", fg=PINK, font=(FONT_NAME, 35, "bold"))
    else:
        countdown_timer(work_seconds)
        status.config(text="Work", fg=GREEN, font=(FONT_NAME, 35, "bold"))


def countdown_timer(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    if count >= 0:
        global timer

        canvas.itemconfig(timer_count, text=f"{minutes}:{seconds}")
        timer = window.after(1000, countdown_timer, count - 1)
    else:
        start_timer()
        marks = ""

        for _ in range(math.floor(Reps/2)):
            marks += "✓"
        check_mark.config(text=marks)


status = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
status.grid(column=1, row=0)

canvas = Canvas(width=200, height=225, bg=YELLOW, highlightthickness=0)
photo_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=photo_img)
timer_count = canvas.create_text(100, 129, fill="white", text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

check_mark = Label(fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
check_mark.grid(column=1, row=3)

start_btn = Button(text="Start", highlightthickness=1, fg=GREEN, command=start_timer)
reset_btn = Button(text="Reset", highlightthickness=1, fg=GREEN, command=reset_timer)
start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)

window.mainloop()
