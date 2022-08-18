from turtle import *
import random as r

tim = Turtle()
tim.shape("turtle")
tim.color("green")
# for d in range(4):
#     tim.right(90)
#     tim.forward(100)

# for i in range(20):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

colormode(255)


def random_color():
    red = r.randint(0, 255)
    green = r.randint(0, 255)
    blue = r.randint(0, 255)
    return red, green, blue

# for i in range(11):
#     tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
#     for j in range(i + 3):
#         tim.forward(100)
#         tim.right(360/(i + 3))tim.speed("fastest")


# tim.pensize(10)
# directions = [0, 90, 180, 270]
#
# for i in range(100):
#     tim.color(random_color())
#     tim.speed(r.randint(1, 10))
#     tim.forward(r.randint(20, 50))
#     tim.setheading(r.choice(directions))

tim.speed("fastest")

for i in range(0, 361, 5):
    tim.circle(100)
    tim.color(random_color())
    tim.setheading(i)

screen = Screen()
screen.exitonclick()
