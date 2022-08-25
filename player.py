from turtle import Turtle

MOVE = 20
STARTING_POINT = (0, -280)

class Player(Turtle):
    """_summary_

    Args:
        Turtle (_type_): _description_
    """

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POINT)
        self.shape("turtle")
        self.setheading(90)
    
    def go_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE)

    def reset(self):
        self.goto(STARTING_POINT)
