from audioop import cross
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"



# my_image = PhotoImage(file="path/to/image_file.png")
# button = Button(image=my_image, highlightthickness=0)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=2)
front_card = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_card)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))

canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0)

cross_image = PhotoImage("images/wrong.png")
unknown_button = Button(image=)

# front_back = PhotoImage(file="images/card_back.png")
# canvas.create_image(400, 263, image=front_back)
# canvas.grid(column=1, row=1)













window.mainloop()
