from tkinter import *


def button_clicked():
    miles = float(input.get())    
    number_text.config(text=miles * 1.689) # the label takes the inputed button when the click button si clicked

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

input = Entry(width=10)
input.grid(column=2, row=1)

miles_text = Label(text="Miles", font=("Arial", 12))
miles_text.grid(column=3, row=1)
miles_text.config(padx=10, pady=10)

isequal_text = Label(text="is equal to", font=("Arial", 12))
isequal_text.grid(column=1, row=2)
isequal_text.config(padx=10, pady=10)

km_text = Label(text="Km", font=("Arial", 12))
km_text.grid(column=3, row=2)
km_text.config(padx=10, pady=10)
    
#Button
calc_button = Button(text="Calculate", command=button_clicked)
calc_button.grid(column=2, row=3)
calc_button.config(padx=10, pady=10)

number_text = Label (text="0", font=("Arial", 12))
number_text.config(text="0")
number_text.grid(column=2, row=2)






window.mainloop()


