from turtle import Turtle

# option for aligning score text
ALIGN = "center"
# tuple containing font, fontsize and font option
FONT = ("Times New Roman", 20, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.update_text()

    def add_level(self):
        self.level += 1
        self.update_text()

    def update_text(self):
        self.clear()
        self.goto((-230, 260))
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto((0, 0))
        self.write("GAME OVER", align=ALIGN, font=FONT)