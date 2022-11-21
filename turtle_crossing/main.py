
from turtle import Screen, Turtle
import time
from car_manager import CarManager
from player import STARTING_POSITION, Player
from scoreboard import Scoreboard

#create screen
screen = Screen()
screen.bgcolor('black')
screen.title("Turtle cross road")
screen.setup(width=600,height=600)

screen.tracer(0)
#boundaries drawer
drawer = Turtle()
drawer.color('orange')
drawer.pen(fillcolor="black", pencolor="dark orange", pensize=5)
#draw bottom line
drawer.penup()
drawer.goto(-300,-250)
drawer.pendown()
drawer.goto(300,-250)
#draw top line
drawer.penup()
drawer.goto(-300,250)
drawer.pendown()
drawer.goto(300,250)
drawer.hideturtle()

#player and cars
daredevil = Player()
traffic = CarManager()
scoreboard = Scoreboard(daredevil.level)
screen.listen()
screen.onkey(daredevil.move,"Up")

game_on = True
while_count = 1

while game_on:
    screen.update()
    time.sleep(0.1)
    
    #generate car every 6 counts
    traffic.crete_car()
    traffic.move()

    for car in traffic.cars:
        if daredevil.distance(car) < 20:
            game_on = False
            print("GAME OVER") 
    
    if daredevil.ycor() > 250:
        daredevil.level += 1
        daredevil.goto(STARTING_POSITION)
        traffic.increase_speed()
        scoreboard.update_scoreboard(daredevil.level)
    while_count +=1






screen.exitonclick()