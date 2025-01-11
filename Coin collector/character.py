from turtle import Turtle
import random

MOVE_DISTANCE = 50

class Character(Turtle):

    def __init__(self):
        super().__init__()
        self.shapesize(1,1)
        self.penup()
        self.goto(0,0)
        self.move = MOVE_DISTANCE

    def move_right(self):
        self.setheading(0)
        self.forward(self.move)

    def move_left(self):
        self.setheading(180)
        self.forward(self.move)

    def move_up(self):
        self.setheading(270)
        self.forward(self.move)

    def move_down(self):
        self.setheading(90)
        self.forward(self.move)