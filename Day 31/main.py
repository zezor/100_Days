import random

import pandas
from tkinter import *

from pandas import DataFrame

BACKGROUND_COLOR = "#B1DDC6"




# ---------------------------- BUTTONS FUNCTIONALITY ------------------------------- #
def check_button_select():
    data = pandas.read_csv("data/french_words.csv")

    data_dict = data.to_dict(orient="records")
    rand_num = random.randint(0, 40)
    dict_selected = data_dict[rand_num]

    key1 = "French"
    key2 = "English"
    word =  dict_selected[key1]
    canvas.create_text(400, 263,text="")
    canvas.create_text(400, 263, text=word, font=("Ariel", 40, "bold"))

# for key  value in data_dict[rand_num]


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#CANVAS WITH IMAGES AND TEXT
canvas = Canvas(width=800, height=526, highlightthickness=2)
front_card = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_card)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))

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
