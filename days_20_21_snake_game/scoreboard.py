from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.goto(0, 470)
        self.score = 0
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()
