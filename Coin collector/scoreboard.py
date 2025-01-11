from turtle import Turtle
from time import sleep

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(x = -600,y = 350)

    def increase_score(self):
        self.score += 1

    def update_score(self):
        self.clear()
        self.write(f'|Score: {self.score}|', font =('Ariel', 30, 'bold'))
