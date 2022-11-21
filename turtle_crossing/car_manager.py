'''
Create cars that are 20px high by 40px wide 
that are randomly generated along the y-axis and move to the left edge of the screen. 
No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). 
Hint: generate a new car only every 6th time the game loop runs.
If you get stuck, check the video walkthrough in Step 4.
'''
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.velocity = STARTING_MOVE_DISTANCE    
    
    def crete_car(self):
        if random.randint(1,16) % 6 == 0:
            new_car = Turtle()
            new_car.shape('square')
            new_car.resizemode('user')
            new_car.penup()
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            self.start_x = 280
            self.start_y = random.randint(-250,250)
            new_car.goto(self.start_x,self.start_y)
            self.cars.append(new_car)
        else:
            pass


    def move(self):
        for car in self.cars:
            car.forward(self.velocity)

    def increase_speed(self):
        self.velocity += MOVE_INCREMENT


        