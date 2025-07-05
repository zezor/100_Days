import random

import pandas
from tkinter import *

from pandas import DataFrame

BACKGROUND_COLOR = "#B1DDC6"


data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")
current_card = {]
# ---------------------------- BUTTONS FUNCTIONALITY ------------------------------- #
def check_button_select():
    rand_num = random.choice(data_dict)
    word_selected = rand_num["French"]
    # word =  dict_selected[key1]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=word_selected)

def flip_card():
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=word_selected)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.after(3000, func=flip_card)


#CANVAS WITH IMAGES AND TEXT
canvas = Canvas(width=800, height=526, highlightthickness=2)
front_card = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_card)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))

canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, columnspan=2, row=0)



#BUTTONS
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image)
unknown_button.grid(row=1, column=0)


check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, command=check_button_select)
check_button.grid(row=1, column=1)


# front_back = PhotoImage(file="images/card_back.png")
# canvas.create_image(400, 263, image=front_back)
# canvas.grid(column=1, row=1)


window.mainloop()
