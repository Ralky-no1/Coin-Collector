from turtle import Screen
import time
from character import Character
from coins import Coins
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width = 1200, height = 800)
screen.bgcolor('black')
screen.tracer(0)
screen.register_shape('wizard.com.gif')



wizard = Character()
wizard.shape('wizard.com.gif')
coins = Coins()
score = Scoreboard()

screen.listen()
screen.onkey(fun = wizard.move_right, key = 'D')
screen.onkey(fun = wizard.move_up, key = 'S')
screen.onkey(fun = wizard.move_down, key = 'W')
screen.onkey(fun = wizard.move_left, key = 'A')

def check_coins_collected():
    global coins, wizard
    for coin in coins.coins:
        if wizard.distance(coin) < 50:
            coin.goto(3000,3000)
            del coin
            score.increase_score()


playing_game = True
while playing_game:
    time.sleep(0.01)
    screen.update()
    coins.create_coins()

    check_coins_collected()

    score.update_score()

screen.exitonclick()