from turtle import Turtle, Screen, color

#create turtle
timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkCyan")

#show window
my_screen = Screen()
print(my_screen.canvheight)

#angle = 360 deg / number of sides of shape
shapes = 7 # triagle to decagon
for i in range(3,11,1):
    colors = ("red","green","blue","black","purple","cyan","gold")
    timmy.color(colors[i-3])
    for j in range(i):
        timmy.forward(100)
        timmy.right(360/i)

#close window
my_screen.exitonclick()