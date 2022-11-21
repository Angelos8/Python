from turtle import Turtle, Screen, colormode
import random



def random_walk(n):
    #create turtle
    timmy = Turtle()
    timmy.shape("turtle")
    timmy.color("DarkCyan")
    timmy.width(4)
    direction = [0,90,180,270]

    #random color
    colormode(255)
    def generate_color():
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        palette = (red, green, blue)
        return palette
        
    #show window
    my_screen = Screen()
    my_screen.bgcolor("black")
    print(my_screen.canvheight)

    #walk
    for _ in range(n):
        timmy.speed(10) #speed range: 0 - 10
        timmy.color(generate_color())
        timmy.forward(50)
        timmy.setheading(random.choice(direction))


    #close window
    my_screen.exitonclick()


#steps
steps = int(input("Enter number of steps: "))
random_walk(steps)

'''
improvements
move turtle within the screen boundaries only
thicken the color line
make background dark

'''
