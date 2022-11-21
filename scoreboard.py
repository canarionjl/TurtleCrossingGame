from turtle import Turtle

FONT = ('Arial', 24, 'bold')
ALIGNMENT = "center"

VERTICAL_POSITION = 270
HORIZONTAL_POSITION = -450


class Scoreboard(Turtle):

    def __init__(self, difficulty):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.hideturtle()
        self.color("black")

        self.update_scoreboard(difficulty)

    def update_scoreboard(self, difficulty):
        self.clear()
        self.goto(HORIZONTAL_POSITION, VERTICAL_POSITION)
        self.write(f"Level: {difficulty}", move=False, align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, -VERTICAL_POSITION-35)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)


