from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
INCREASE_PER_SCORE = 2

STARTING_POSITIONS = [(randint(-280,280),randint(-250,260)) for _ in range(20)]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.penup()
        self.hideturtle()
        

    def generate_cars(self):
        for position in STARTING_POSITIONS:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1,2)
            new_car.color(choice(COLORS))
            new_car.goto(position)
            self.cars.append(new_car)
    
    def move_cars(self, score):
        for car in self.cars:
            if car.xcor() > -280:
                car.backward(STARTING_MOVE_DISTANCE + score * INCREASE_PER_SCORE)
            else:
                car.goto(280, car.ycor())
                