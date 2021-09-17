from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def forward_move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def backward_move(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if self.ycor() > -280:
            self.goto(self.xcor(), new_y)

    def first_place(self):
        self.goto(STARTING_POSITION)

    def collision(self, obstacle):
        self.distance(obstacle)

