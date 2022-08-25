from turtle import Screen
from player import Player
from cars import CarManager
from scoreboard import Scoreboard
import time


WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_on = True
count = 0
count_limit = 30
while game_on:
    time.sleep(0.01)
    if count == count_limit:
        car_manager.add_car()
        count = 0
    car_manager.move_car()
    

    # Detect collisions
    for car in car_manager.car_list:
        if abs(car.xcor() - player.xcor()) <= 30 and abs(car.ycor() - player.ycor()) <= 20:
            game_on = False
            scoreboard.game_over()

    # Detect crossed street
    if player.ycor() > 250:
        player.reset()
        car_manager.level_up()
        scoreboard.add_level()
        
        if scoreboard.level % 2 == 0:
            count_limit -= 3
            
    screen.update()
    count += 1
screen.exitonclick()

