from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.ht()
        self.score = 1
        self.update()

    def update(self):
        self.clear()
        self.goto(0, 290)
        self.write(f"Level {self.score}", align="center", font=("courier", 24, "normal"))

    def level_up(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("courier", 70, "normal"))
