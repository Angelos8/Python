'''
Create a turtle player that starts at the bottom of the screen 
and listen for the "Up" keypress to move the turtle north. 
If you get stuck, check the video walkthrough in Step 3

'''
from tkinter import DISABLED
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('red')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.level = 1

    def move(self):
        self.forward(MOVE_DISTANCE)
        

    
