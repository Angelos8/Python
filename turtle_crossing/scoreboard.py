FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,level):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(-200,260)
        self.level = level
        self.update_scoreboard(self.level)
    
    def update_scoreboard(self,level):
        self.clear()
        self.level = level
        self.write(f'Level: {self.level}', align='center',font=FONT)
    

        pass
    
