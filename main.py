from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global marks
    window.after_cancel(timer)
    reps = 0
    print(reps)
    label_check.config(text="", bg=YELLOW)
    label_timer.config(text="TIMER", fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work = WORK_MIN
    short_break = SHORT_BREAK_MIN
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_timer.config(text="LONG BREAK", font=(FONT_NAME, 32, "bold"), fg=RED, bg=YELLOW)
        countdown(long_break)

    elif (reps % 2) == 0:

        label_timer.config(text="BREAK", font=(FONT_NAME, 32, "bold"), fg=PINK, bg=YELLOW)
        countdown(short_break)

    else:

        label_timer.config(text="WORK", font=(FONT_NAME, 32, "bold"), fg=GREEN, bg=YELLOW)
        countdown(work)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# Recursion- calling function inside a function
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        index_cycle = 0
        work_session = math.floor(reps / 2)
        print(work_session)
        for _ in range(work_session):
            index_cycle += 1
            marks += f"cycle {index_cycle}:✔"
        if work_session == 2:
            label_check.grid(column=1, row=4)
            label_check.config(text=marks)

        label_check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_timer = Label(text="TIMER")
label_timer.config(font=(FONT_NAME, 32, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)

# specify canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Button
button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)

button_start.grid(column=0, row=2)
button_reset.grid(column=2, row=2)

# Checkmark
label_check = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
label_check.grid(column=1, row=3)
window.mainloop()
