from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.shape('square')
        self.resizemode('user')
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color('white')
        self.goto(pos_x,pos_y)

    def move_up(self):
        self.goto(self.xcor(),self.ycor() + 20)
        

    def move_down(self):
        self.goto(self.xcor(),self.ycor() - 20)

        
        
    