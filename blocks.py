import math
import random
from turtle import Turtle
import random

VERTICAL_MARGIN_POSITION = 220
HORIZONTAL_INITIAL_POSITION = 520
COLORS = ["red", "blue", "purple", "orange", "yellow", "green", "pink"]


def generate_color():
    return random.choice(COLORS)


def generate_position():
    y_cor = random.randint(-VERTICAL_MARGIN_POSITION, VERTICAL_MARGIN_POSITION)
    x_cor = HORIZONTAL_INITIAL_POSITION
    position = (x_cor, y_cor)
    return position


class Block:

    def __init__(self, difficulty):
        self.all_blocks = []
        self.generate_blocks(difficulty)

    def move(self, difficulty):
        for block in self.all_blocks:
            if difficulty > 1:
                difficulty = math.log(difficulty, 2)
            block.forward(15 * difficulty)

    def generate_blocks(self, difficulty):
        n_blocks = random.randint(0, difficulty)
        for _ in range(n_blocks):
            positions = []
            block = Turtle()
            block.penup()
            block.shape("square")
            block.setheading(180)
            block.shapesize(1, 2)
            color = generate_color()
            block.color(color)
            while True:
                position = generate_position()
                if position not in positions:
                    break
            block.goto(position)
            positions.append(position)
            self.all_blocks.append(block)


