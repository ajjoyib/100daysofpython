# D27 PROJECT - MILE TO KM CONVERTER
from tkinter import *
from tkinter import ttk as t


def mile_to_km_conv(*args):
    mile_input = mile_entry.get()
    km_output = int(mile_input) * 1.6
    result_label["text"] = str(km_output)


root_window = Tk()
root_window.minsize(width=200, height=100)
root_window.title("Mile to Km Converter")

frame_widget = t.Frame(root_window, padding=20)
frame_widget.grid()

mile_entry = t.Entry(frame_widget, width=10)
mile_entry.grid(column=2, row=1)

mile_label = t.Label(frame_widget, text="Miles")
mile_label.grid(column=3, row=1)

equal_label = t.Label(frame_widget, text="is equal to")
equal_label.grid(column=1, row=2)

result_label = t.Label(frame_widget, text="0")
result_label.grid(column=2, row=2)

km_label = t.Label(frame_widget, text="Km")
km_label.grid(column=3, row=2)

calculate_btn = t.Button(frame_widget, text="Calculate", command=mile_to_km_conv)
calculate_btn.grid(column=2, row=3)

root_window.mainloop()