from turtle import Turtle

INITIAL_POSITION = (0, -290)


class MyTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shapesize(1.5, 1.5)
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.initial_position()

    def move(self):
        self.forward(15)

    def initial_position(self):
        self.goto(INITIAL_POSITION)
