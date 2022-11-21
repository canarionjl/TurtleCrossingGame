import math
import time
from scoreboard import Scoreboard
from turtle import Screen, Turtle
from blocks import Block
from my_turtle import MyTurtle

VERTICAL_DIMENSION = 650
HORIZONTAL_DIMENSION = 1000
VERTICAL_BORDER_PADDING = 150
HORIZONTAL_BORDER_PADDING = 80

difficulty = 1
game_is_on = True


def configure_screen(screen_passed):
    screen_passed.setup(width=HORIZONTAL_DIMENSION, height=VERTICAL_DIMENSION)
    screen_passed.bgcolor("white")
    screen_passed.title("Ping Pong Game")
    screen_passed.tracer(0)
    screen_passed.listen()
    create_border_square()


def create_border_square():
    sign = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    hor_border_value = int((HORIZONTAL_DIMENSION - HORIZONTAL_BORDER_PADDING) / 2)
    ver_border_value = int((VERTICAL_DIMENSION - VERTICAL_BORDER_PADDING) / 2)
    border = Turtle()
    border.color("black")
    for sign_ in sign:
        if border.isdown():
            border.penup()
        else:
            border.pendown()
        border.goto(hor_border_value * sign_[0], ver_border_value * sign_[1])
    border.hideturtle()


def difficulty_adapter():
    if difficulty == 1:
        return 1
    elif difficulty > 1:
        return math.log(difficulty, 2)


my_screen = Screen()
configure_screen(my_screen)

myTurtle = MyTurtle()
my_screen.onkey(myTurtle.move, "Up")

my_blocks = Block(difficulty)

scoreboard = Scoreboard(difficulty)
scoreboard.update_scoreboard(difficulty)

counter = 1
timer = 0.1

while game_is_on:
    my_screen.update()
    time.sleep(timer / difficulty_adapter())
    if counter % 5 == 0:
        my_blocks.generate_blocks(difficulty)
    my_blocks.move(difficulty)
    counter += 1

    for element in my_blocks.all_blocks:
        if myTurtle.distance(element) < 30 and myTurtle.xcor() + 20 < element.xcor():
            game_is_on = False
            scoreboard.game_over()

    if myTurtle.ycor() >= 250:
        myTurtle.initial_position()
        difficulty += 1
        scoreboard.update_scoreboard(difficulty)

my_screen.exitonclick()
