""" Module containing class Player and modeling the behaviour of the objects.

Classes:
    Player(Turtle)

Methods:
    go_up()
        move player up
    reset()
        reset player to the initial position

Constants:
    MOVE
        distance that turtle makes with each step
    STARTING_POINT
        starting point of the turtle after each reset
"""


from turtle import Turtle

# Distance that turtle makes with each step
MOVE = 20
# Starting point of the turtle after each reset
STARTING_POINT = (0, -280)

class Player(Turtle):
    """Creates turtle controlled by user.

    Args:
        Turtle (class): superclass of the Player class
    """

    def __init__(self):
        """Create player object at its initial position.
        """

        super().__init__()
        self.penup()
        self.goto(STARTING_POINT)
        self.shape("turtle")
        self.setheading(90)
    
    def go_up(self):
        """Move player up
        """

        self.goto(self.xcor(), self.ycor() + MOVE)

    def reset(self):
        """Reset player to his initial position
        """
        
        self.goto(STARTING_POINT)
