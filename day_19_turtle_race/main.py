from turtle import Turtle, Screen

dim = Turtle()
screen = Screen()


def move_forwards():
    dim.forward(10)


def move_backwards():
    dim.back(10)


def turn_right():
    new_heading = dim.heading() - 10
    dim.setheading(new_heading)


def turn_left():
    new_heading = dim.heading() + 10
    dim.setheading(new_heading)


def clear_draw():
    dim.clear()
    dim.penup()
    dim.home()
    dim.pendown()


def print_xcor():
    print(dim.xcor())


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_draw)
screen.onkey(key="p", fun=print_xcor)
screen.exitonclick()
