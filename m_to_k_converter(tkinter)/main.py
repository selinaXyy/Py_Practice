from tkinter import *

window = Tk()
window.title("Mile to Kilometers Converter")
window.minsize(width=200, height=50)
window.config(padx=20, pady=20)

#entry
input_miles = Entry(text="0", width=10)
input_miles.grid(row=0, column=1)

#label
lbl_miles = Label(text="Miles")
lbl_is_equal_to = Label(text="is equal to")
lbl_converted_km = Label(text="0")
lbl_km = Label(text="Km")

lbl_is_equal_to.grid(row=1, column=0)
lbl_converted_km.grid(row=1, column=1)
lbl_miles.grid(row=0, column=2)
lbl_km.grid(row=1, column=2)

#button
def convert_to_km():
    miles = float(input_miles.get())
    converted_km = round(miles * 1.6, 2)
    lbl_converted_km["text"] = converted_km

btn_calculate = Button(text="Calculate", command=convert_to_km)
btn_calculate.grid(row=2, column=1)

window.mainloop()