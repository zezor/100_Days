import tkinter
#import tkinter
#windows = tkinter.Tk()
windows = tkinter.Tk()
windows.title("My First GUI Programme")
windows.minsize(width=500, height=300)
windows.config(padx=10, pady=10)  #adding a padding


#Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 14, "bold"))
my_label.config(text="New Text")
#my_label.pack()
#my_label.place(x=100, y=180)  #changing position
my_label.grid(column=0, row=0)  #changing position
my_label.config(padx=5, pady=5)  #adding a padding

#Button
def buttonclicked():
    input_text = input.get()
    my_label.config(text = input_text)

my_label["text"] = "New Text"
my_label.config(text="New Text")


new_button = tkinter.Button(text ="Click Me", command=buttonclicked)
#button.pack()
#button.place(x= 100, y=220)
new_button.grid(column= 2, row= 0)

button = tkinter.Button(text ="Click Me", command=buttonclicked)
#button.pack()
#button.place(x= 100, y=220)
button.grid(column= 1, row= 1)



my_label["text"] = "New Text"
my_label.config(text="New Text")

#Entry
input =tkinter.Entry(width= 50)
print(input.get())
#input.pack()
#input.place(x= 100, y=250)
input.grid(column= 4, row= 3)











windows.mainloop()
