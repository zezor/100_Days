from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")


#placing canvas for the padlock
canvas = Canvas(width=200, height=200,bg="white", highlightthickness=2, highlightbackground="black")
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=padlock_img )
canvas.grid(column= 2, row=3)

website_name_entry = Entry(width=35)
website_name_entry.grid(row=4, column = 1, columnspan=3)

email_entry = Entry(width=35)
email_entry.grid(row=5, columnspan=3)

website_label = Label(text="Website")
website_label.grid(row=4, column=0)





window.mainloop()
