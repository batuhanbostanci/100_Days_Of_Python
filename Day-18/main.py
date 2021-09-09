import turtle as t
from turtle import Screen
import random

timm = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        timm.speed("slow")
        timm.color(random_color())
        timm.circle(100)
        print(timm.heading() + 10, "\n")
        timm.setheading(timm.heading() + size_of_gap)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()
