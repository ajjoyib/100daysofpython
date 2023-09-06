from turtle import Turtle, Screen
import random

colors = ["blue violet", "medium violet red", "deep pink", "crimson", "red", "orange red", "dark orange", "gold",
          "yellow", "yellow green", "lime", "aquamarine", "dark cyan", "steel blue", "dodger blue", "blue", "light steel blue",
          "light slate gray", "gray", "black"]
tom = Turtle()

def shape_draw(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tom.forward(100)
        tom.right(angle)


for shape_side_n in range (3, 11):
    tom.color(random.choice(colors))
    drawing_shape(shape_side_n)








screen = Screen()
screen.exitonclick()
