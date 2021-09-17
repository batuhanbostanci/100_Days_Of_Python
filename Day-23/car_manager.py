from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.new_speed = STARTING_MOVE_DISTANCE

    def create_new_car(self):
        temp = random.randint(1, 5)
        if temp == 1:
            turtle = Turtle()
            turtle.penup()
            turtle.shape("square")
            turtle.shapesize(stretch_wid=1, stretch_len=2)
            color = random.choice(COLORS)
            turtle.color(color)
            x_cor = 300
            y_cor = random.randint(-250, 300)
            turtle.goto(x_cor, y_cor)
            self.cars.append(turtle)

    def move(self):
        for i in self.cars:
            i.forward(-self.new_speed)

    def increase_speed(self):
        self.new_speed += MOVE_INCREMENT

