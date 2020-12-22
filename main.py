import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
carmanager = CarManager()

screen.listen()

screen.onkey(player.up, 'Up')

game_is_on = True
carmanager.generate_cars()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() >= 280:
        player.finish()
        scoreboard.add_one()
    
    #Detect collision with car
    for car in carmanager.cars:
        if player.distance(car) <=25:
            scoreboard.game_over()
            game_is_on = False
    carmanager.move_cars(scoreboard.score)
    
        
        





screen.exitonclick()