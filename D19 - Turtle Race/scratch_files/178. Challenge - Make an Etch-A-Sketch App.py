from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def rotate_clockwise():
    # tim.right(10)
    tim.setheading(tim.heading() - 10)


def rotate_counter_clockwise():
    # tim.left(10)
    tim.setheading(tim.heading() + 10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=rotate_clockwise, key="d")
screen.onkey(fun=rotate_counter_clockwise, key="a")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
