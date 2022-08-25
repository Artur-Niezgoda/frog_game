from turtle import Screen
from player import Player
from cars import CarManager

import time

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_on = True
count = 0
while game_on:
    time.sleep(0.01)
    if count == 30:
        car_manager.add_car()
        count = 0
    car_manager.move_car()
    

    # Detect collisions
    for car in car_manager.car_list:
        if abs(car.xcor() - player.xcor()) <= 30 and abs(car.ycor() - player.ycor()) <= 20:
            game_on = False

    if player.ycor() > 250:
        player.reset()
        car_manager.level_up()
    screen.update()
    count += 1
screen.exitonclick()

# TODO: Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). 
# When this happens, return the turtle to the starting position and increase the speed of the cars. 
# Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. 

# TODO: Create a scoreboard that keeps track of which level the user is on. 
# Every time the turtle player does a successful crossing, the level should increase. 
# When the turtle hits a car, GAME OVER should be displayed in the centre. 
