from tkinter import *

def button_clicked():
    text = input.get()
    res = float(text) * 1.61
    output.config(text=res)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)

#Label
label = Label(text="is equal to", font=("Arial", 24, "bold"))
label.grid(column=0, row=1)

#output
output = Label(text="0", font=("Arial", 24, "bold"))
output.grid(column=1, row=0)


#units
miles = Label(text="Miles")
miles.grid(column=2, row=0)
km = Label(text="Km")
km.grid(column=2, row=1)

#entry
input = Entry(width=10)
input.grid(column=1, row=0)


#button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)






# needs to be at end of program
window.mainloop()

