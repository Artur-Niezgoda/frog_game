from turtle import Turtle
import random

NUMBER_OF_CARS = 20
CAR_COLORS = ["red", "orange", "yellow", "green", "blue", "violet"]
# CAR_SPEEDS = {"red": 3, "orange": 2.5, "yellow": 2, "green": 1.5, "blue": 1, "violet": 0.5}
STARTING_MOVE_SPEED = 1
SPEED_INCREMENT = 1

class CarManager:
    
    def __init__(self):
        self.car_list = []
        self.speed = STARTING_MOVE_SPEED

    def add_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(CAR_COLORS))
        new_car.goto((300, random.randint(-240, 240)))
        self.car_list.append(new_car)


    def move_car(self):
        for car in self.car_list:
            car.backward(self.speed)
            if car.xcor() < -320:
                car.hideturtle()
                self.car_list.remove(car)


    def level_up(self):
            self.speed += SPEED_INCREMENT
        

