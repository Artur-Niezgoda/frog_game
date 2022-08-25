"""Module consisting class that allows to create new cars and manage traffic.

Classes:
    CarManager

Methods:
    add_car
        add new car to the traffic
    move_car
        move car from right to left and remove it if it goes beyond screen
    level_up
        increse speed of the cars

Constants:
    CAR_COLORS
        list of colors for cars
    STARTING_MOVE_SPEED
        initial speed
    SPEED_INCREMENT
        speed increase with each level
"""


from turtle import Turtle
import random

NUMBER_OF_CARS = 20
CAR_COLORS = ["red", "orange", "yellow", "green", "blue", "violet"]
# CAR_SPEEDS = {"red": 3, "orange": 2.5, "yellow": 2, "green": 1.5, "blue": 1, "violet": 0.5}
STARTING_MOVE_SPEED = 1
SPEED_INCREMENT = 1

class CarManager:
    """Create and manage car traffic during the game

    Attributes:
        car_list (list): list of cars - Turtle objects, empty by default 
        speed: current value of the speed of the cars, default STARTING_MOVE_SPEED
    """

    def __init__(self):
        """Create and empty list, an object of the CarManager
        """
        self.car_list = []
        self.speed = STARTING_MOVE_SPEED

    def add_car(self):
        """Create a new car and add it to the car_list.
        """

        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(CAR_COLORS))
        new_car.goto((300, random.randint(-240, 240)))
        self.car_list.append(new_car)


    def move_car(self):
        """Move a car and if goes beyond the screen remove it.
        """

        for car in self.car_list:
            car.backward(self.speed)
            if car.xcor() < -320:
                car.hideturtle()
                self.car_list.remove(car)

    def level_up(self):
        """Increase the speed of the cars.
        """
        
        self.speed += SPEED_INCREMENT
        
