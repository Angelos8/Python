
from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboared
import time

#set screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

#computer = Paddle(350,0)
left_paddle = Paddle(-350,0)
right_paddle =  Paddle(350,0)
ball = Ball()
scoreboared = Scoreboared()

#enable paddle control
screen.listen()
screen.onkey(right_paddle.move_up,"Up")
screen.onkey(right_paddle.move_down,"Down")
screen.onkey(left_paddle.move_up,"w")
screen.onkey(left_paddle.move_down,"s")

game_on = True
while game_on:
    #once trace is on, in order for graphics to appear, 
    #we need manual to update to screen everytime,
    #hence the while loop
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #bouncing off wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    
    #bouncing off paddles
    elif ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #if ball is missed by the paddles
    if ball.xcor() > 380: 
        ball.reset_posititon()
        scoreboared.left_point()
    
    if ball.xcor() < -380:
        ball.reset_posititon()
        scoreboared.right_point()



screen.exitonclick()