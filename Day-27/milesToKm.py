from tkinter import *
import math
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=40)
window.config(padx=10, pady=10)

input = Entry(width=10)
input.grid(column=1, row=0)

label_1 = Label(text="Miles")
label_1.grid(row=0, column=2)

label_2 = Label(text="is equal to")
label_2.grid(row=1, column=0)

label_3 = Label(text="Km")
label_3.grid(row=1, column=2)

label_4 = Label(text="0")
label_4.grid(row=1, column=1)


def get_clicked():
    new_input = input.get()
    calculation = float(new_input) * 1.2
    round(calculation, 2)
    # label_4.config(text=float("{:.2f}".format(calculation)))

    label_4.config(text=calculation)

button = Button(text="Calculate", command =get_clicked)
button.grid(row=2, column=1)

window.mainloop()