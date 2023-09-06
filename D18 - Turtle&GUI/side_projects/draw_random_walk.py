import turtle as t
import random as rnd

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = rnd.randint(0, 255)
    g = rnd.randint(0, 255)
    b = rnd.randint(0, 255)
    rnd_color = (r, g, b)
    return rnd_color


directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")

for _ in range(2000):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(rnd.choice(directions))

screen = t.Screen()
screen.exitonclick()
