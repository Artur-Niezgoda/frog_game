"""Module displaying current level and game over if player looses.

Class:
    Scoreboard(Turtle)

Methods:
    add_level()
        add level whenever player crosses the street successfully
    update_text()
        update text with current level value
    game_over()
        display text GAME OVER when player looses

Constants:
    ALIGN
        option for aligning level text
    FONT
        tuple containing font, fontsize and font option
"""

from turtle import Turtle

# option for aligning score text
ALIGN = "center"
# tuple containing font, fontsize and font option
FONT = ("Times New Roman", 20, "bold")

class Scoreboard(Turtle):
    """Class creating a level text on the top of the screen

    Args:
        Turtle (class): superclass of Scoreboard class

    Attributes:
        level (int): level number, default 0 
    """

    def __init__(self):
        """Creates object that displays score
        """

        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.update_text()

    def add_level(self):
        """Add level to the current value and update the text
        """

        self.level += 1
        self.update_text()

    def update_text(self):
        """Update the text with the current value of level
        """

        self.clear()
        self.goto((-230, 260))
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        """Print GAME OVER when player loses.
        """

        self.goto((0, 0))
        self.write("GAME OVER", align=ALIGN, font=FONT)