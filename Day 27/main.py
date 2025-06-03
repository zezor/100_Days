import tkinter
windows = tkinter.Tk()
windows.title("My First GUI Programme")
windows.minsize(width=500, height=300)


#Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24,"bold"))
my_label.pack(side="left")










windows.mainloop()