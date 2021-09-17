import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
new_car = CarManager()

screen.onkey(player.forward_move, "Up")
screen.onkey(player.backward_move, "Down")

scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    new_car.create_new_car()
    new_car.move()

    # Detect collision with cars
    for i in new_car.cars:
        if i.distance(player) < 25:
            game_is_on = False
            scoreboard.game_finish()

    if player.ycor() > 280:
        scoreboard.score()
        player.first_place()
        new_car.increase_speed()

screen.exitonclick()