import tkinter
from tkinter.ttk import Button

#import tkinter
#windows = tkinter.Tk()
windows = tkinter.Tk()
windows.title("Miles to Kilometer Programme")
windows.minsize(width=350, height=220)
windows.config(padx= 20, pady=20)

def calculate():
    miles = float(input_figure.get())
    km = round(miles * 1.609,ndigits=2)
    output_label.config(text= f"{km}")


input_figure =tkinter.Entry(width= 10)
input_figure.get()
input_figure.grid(column= 1, row= 0)



miles_label = tkinter.Label(text="Miles", font=("Arial", 14, "bold"))
miles_label.grid(column=2, row=0)  #changing position
miles_label.config(padx=1, pady=1)  #adding a padding


km_label = tkinter.Label(text="Km", font=("Arial", 14, "bold"))
km_label.grid(column=2, row=1)  #changing position
km_label.config(padx=1, pady=1)  #adding a padding

is_equal_to_label = tkinter.Label(text="is equal to", font=("Arial", 14, "bold"))
is_equal_to_label.grid(column=0, row=1)  #changing position
is_equal_to_label.config(padx=1, pady=1)  #adding a padding

output_label = tkinter.Label(text="0", font=("Arial", 14, "bold"))
output_label.grid(column=1, row=2)  #changing position
output_label.config(padx=1, pady=1)  #adding a padding

calculate_button = tkinter.Button(text="Calculate",command=calculate)
calculate_button.grid(column=1, row=4)  #changing position
calculate_button.config(padx=5, pady=5)  #adding a padding

windows.mainloop()