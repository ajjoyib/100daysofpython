# A Hello World Program
from tkinter import *
from tkinter import ttk

# root_window = Tk()
# frame_widget = ttk.Frame(root_window, padding=20)
# frame_widget.grid()
# ttk.Label(frame_widget, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frame_widget, text="Quit", command=root_window.destroy).grid(column=0, row=1)
# root_window.mainloop()

def add(*args):
    sum = 0
    for number in args:
        sum += number
    print(type(args))
    return sum

add(12, 34, 55, 32, 99)

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(type(kwargs))

calculate(2, add=2, multiply=4)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")

my_car = Car(make="Hyundai", model="Sonata")
print(my_car)
