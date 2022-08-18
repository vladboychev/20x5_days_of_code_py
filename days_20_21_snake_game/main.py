from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("blue")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.display_score()

    # Detect collisions with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.grow()

    # Detect collisions with wall
    if snake.head.xcor() > 490 or snake.head.xcor() < -490 or snake.head.ycor() > 490 or snake.head.ycor() < -490:
        game_is_on = False
        scoreboard.game_over()

    # Detect collisions with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
