import turtle as t
import random as rnd

tim = t.Turtle()
t.colormode(255)


def random_rgb_color_generator():
    r = rnd.randint(0, 255)
    g = rnd.randint(0, 255)
    b = rnd.randint(0, 255)
    random_rgb_color = (r, g, b)
    return random_rgb_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_rgb_color_generator())
        tim.speed("fastest")
        tim.circle(100)
        # tim.left(10)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(20)


screen = t.Screen()
screen.exitonclick()
