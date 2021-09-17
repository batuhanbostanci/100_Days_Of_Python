from turtle import Turtle


FONT = ("Courier", 24, "normal")
X_Y_COR = (-280, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.score()

    def score(self):
        self.update_score()
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def update_score(self):
        self.clear()
        self.goto(X_Y_COR)
        self.level += 1

    def game_finish(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)