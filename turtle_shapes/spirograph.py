from logging import PlaceHolder
from turtle import Turtle, Screen, colormode
import random

#Timmy the turtle
timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkCyan")

#random color
colormode(255)
timmy.width(2)
timmy.speed(0)

def generate_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    palette = (red, green, blue)
    return palette

def print_spiral(gap):
    #show window
    my_screen = Screen()
    my_screen.bgcolor("black")
    print(my_screen.canvheight)
    for i in range(int(360/gap)):
        
        timmy.color(generate_color())
        timmy.circle(100,None,None) #circle parameters: (radius, circle arc, steps to take to complete the circle)
        timmy.left(5)
    #close window
    my_screen.exitonclick()

print_spiral(5)