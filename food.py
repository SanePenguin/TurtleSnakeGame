from turtle import Turtle
import random

BUFFER = 20

class Food(Turtle):
    def __init__(self, field_size:tuple) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        self.speed("fastest")
        self.spawn_random(abs_x_bound=field_size[0], abs_y_bound=field_size[1])

    def spawn_random(self, abs_x_bound, abs_y_bound) -> None:
        random_x = random.randint(-(abs_x_bound//2) + BUFFER, abs_x_bound//2 - BUFFER)
        centered_random_x = random_x//20*20
        random_y = random.randint(-(abs_y_bound//2) + BUFFER, abs_y_bound//2 -BUFFER)
        centered_random_y = random_y//20*20
        self.goto(centered_random_x, centered_random_y)