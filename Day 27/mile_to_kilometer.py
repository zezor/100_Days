import tkinter
#import tkinter
#windows = tkinter.Tk()
windows = tkinter.Tk()
windows.title("Miles to Kilometer Programme")
windows.minsize(width=500, height=300)

my_label = tkinter.Label(text="Miles", font=("Arial", 14, "bold"))

my_label.grid(column=3, row=0)  #changing position
my_label.config(padx=5, pady=5)  #adding a padding






input =tkinter.Entry(width= 10)
print(input.get())
#input.pack()
#input.place(x= 100, y=250)
input.grid(column= 4, row= 3)


windows.mainloop()