from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    # Hard level


    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)


    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website= website_name_entry.get()  #getting hold of the entry
    email = email_entry.get()
    password = password_entry.get()


    if len(website) == 0 or len(email) == 0 or len(password) ==0:
        messagebox.showerror(title="Oops!", message="Please don't leave any field empty!")
    else:

         #creating a dialogue or pop up box
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\n Password: {password} \n Is ok to save?")

        if is_ok:
            with open("data.text", "a") as file:
                        file.write(f"{website} / {email} / {password} \n")
            website_name_entry.delete(0, END) # to clear entry box when add button is clicked
            #email_entry.delete(0, END)
            password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


#placing canvas for the padlock
canvas = Canvas(width=200, height=200,bg="white", highlightthickness=2, highlightbackground="black")
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=padlock_img )
canvas.grid(column= 1, row=0)

# ENTRIES
website_name_entry = Entry(width=35)
website_name_entry.grid(row=1, column = 1, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(0, "kemma2993@gmail.com")  #giving a default value to the entry box
email_entry.grid(row=2,column = 1 , columnspan=2)

password_entry = Entry(width=25)
password_entry.grid(row=3,column = 1)


#lABELS
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
#website_label.config(padx=5, pady=5, bg="white")
website_name_entry.focus() # to put the curser in the box run programme starts

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
#email_label.config(padx=5, pady=5, bg="white")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
#password_label.config(padx=5, pady=5, bg="white")


# BUTTONS
generate_password_button = Button(text="Generate Password", command= generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
