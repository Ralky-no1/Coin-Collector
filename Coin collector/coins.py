from turtle import Turtle
from time import sleep
import random

class Coin(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(random.uniform(-570, 570),random.uniform(370,-370))
        self.color('gold')
        self.shape('circle')
        self.shapesize(2,2)

class Coins:

    def __init__(self):
        self.coins = []
        self.create_coins()



    def create_coins(self):
        i = random.randint(1,150)
        if i == 1:
            coin = Coin()
            self.coins.append(coin)
