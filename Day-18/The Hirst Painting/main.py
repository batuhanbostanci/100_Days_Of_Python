from turtle import Screen, Turtle as turta
import colorgram
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     return_color = (r, g, b)
#     rgb_colors.append(return_color)
rgb_colors = [(245, 243, 238), (247, 242, 244), (240, 245, 241), (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

screen = Screen()
screen.colormode(255)
turtle = turta()
turtle.hideturtle()
turtle.speed("fastest")
turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.pendown()
turtle.setheading(0)
number_of_dots = 100
for i in range(1, number_of_dots+1):
    turtle.dot(20, random.choice(rgb_colors))
    turtle.penup()
    turtle.forward(50)
    if i % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)


screen.bgcolor("gray")
screen.exitonclick()