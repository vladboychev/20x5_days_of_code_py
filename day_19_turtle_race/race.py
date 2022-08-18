from turtle import Turtle, Screen
import random

is_race_on = True

dim = Turtle()
dim.color("red")
tim = Turtle()
tim.color("blue")
pim = Turtle()
pim.color("yellow")
vim = Turtle()
vim.color("green")
rim = Turtle()
rim.color("brown")
kim = Turtle()
kim.color("orange")

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


def goto_start(turtle, y):
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(-240, y)


goto_start(dim, -125)
goto_start(tim, -75)
goto_start(pim, -25)
goto_start(vim, 25)
goto_start(rim, 75)
goto_start(kim, 125)

turtles = [dim, tim, pim, vim, rim, kim]

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() == 230:
            winner = turtle.pencolor()
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.speed("normal")
        turtle.forward(random_distance)


if winner == user_choice:
    print(f"The {winner} turtle won the race. You win!")
else:
    print(f"The {winner} turtle won the race. You lose!")

screen.exitonclick()

