from turtle import Screen
import time
from scoreboard import Scoreboared
from snake import Snake
from food import Food


screen = Screen()
screen.setup(height=600, width = 600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0) #turns screen off and does not show the animation of the following steps

snake = Snake()
food = Food()
scoreboard = Scoreboared()

#control movement
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    screen.update() #now the screen is on and shows animation
    time.sleep(0.1)
    snake.move()
    #check if snake is close to food
    if snake.head.distance(food) < 15: #food size (10x10 pixels), so adding a buffer of 5. we check if snake is within 15 pixels.
        print("Deliciousss!")
        food.refresh() #it calls refresh and the food changes location
        snake.extend()
        scoreboard.increase_score()
    
    #deteck collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        scoreboard.reset()
        snake.reset()

    #detect collision with the tail
    #loop through the segments
    for segment in snake.segments[1:]:
        #if the segment is the head then pass. that is because upon creating the snake the head is already close to the tail
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            
screen.exitonclick()
















