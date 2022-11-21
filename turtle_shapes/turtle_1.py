from turtle import Turtle, Screen

#create turtle
timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkCyan")

#show window
my_screen = Screen()
print(my_screen.canvheight)

# #create a square
# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)


for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
   


#close window
my_screen.exitonclick()

