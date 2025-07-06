import random

import pandas
from tkinter import *

from pandas import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ---------------------------- BUTTONS FUNCTIONALITY ------------------------------- #
def check_button_select():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(background_card, image=front_card)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(background_card, image=back_card)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False) #index set to False to delete index in dataframe
    check_button_select()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


#CANVAS WITH IMAGES AND TEXT
canvas = Canvas(width=800, height=526, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
back_card =PhotoImage(file="images/card_back.png")
background_card = canvas.create_image(400, 263, image=front_card)
# back_image = canvas.create_image(400, 263, image=background_card)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))

canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, columnspan=2, row=0)



#BUTTONS
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=check_button_select)
unknown_button.grid(row=1, column=0)


check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, command=is_known)
check_button.grid(row=1, column=1)

#calling out the function below to start with a french word
check_button_select()


window.mainloop()
