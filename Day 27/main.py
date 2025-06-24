from tkinter import *
#import tkinter
#windows = tkinter.Tk()
windows = Tk()
windows.title("My First GUI Programme")
windows.minsize(width=500, height=300)


#Label
my_label = Label(text="I am a Label", font=("Arial", 24,"bold"))
my_label.config(text="New Text")
my_label.pack(side="left")

#Button
def buttonclicked():
    #print(input.get())
    my_label.config(text = input.get())

button = Button(text = "Click Me", command=buttonclicked)
button.pack(side="left")

my_label["text"] = "New Text"
my_label.config(text="New Text")

input =Entry(width=10)
print(input.get())
input.pack(side="left")











windows.mainloop()
