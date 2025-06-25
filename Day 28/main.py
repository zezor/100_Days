import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    '''Reset the timer, clear checkmarks, when called'''
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= '00:00')
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #if it's  the 1st/3rd/5th/7th rep:
    if reps % 2 != 0:
        count_down(work_sec)
        title_label.config(text="Work", fg=RED)

    # if it's  the 2n/4h/6th rep:
    elif reps % 2 ==0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        # if it's the 8th rep:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec ==0:
        count_sec = "00"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# creating the window
window = Tk()
window.title("Pomodore")
window.config(padx=100, pady=50, bg=YELLOW)


#placing canvas for the tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,110, image=tomato_img )
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column= 2, row=3)


#Timer Label
title_label= Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=2, row=0)
title_label.config(padx=6, pady=6)

#Start Button
start_button = Button(text="Start", width=7, highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=4)

#Reset Button
reset_button = Button(text="Reset", width=7, highlightthickness=0, command=reset_timer)
reset_button.grid(column=6, row=4)

check_marks = Label(text= "", fg=GREEN, bg=YELLOW)
check_marks.grid(column=2, row= 5)




window.mainloop()