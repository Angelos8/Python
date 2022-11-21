from turtle import Turtle

#constants
ALIGNMENT = "center"
FONT = ("Arial",8,"normal")
class Scoreboared(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
    
    #function updates the scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score:{self.highscore}",align=ALIGNMENT,font=FONT)
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",'w') as data:
                data.write(str(self.highscore))
            
        self.score = 0
        self.update_scoreboard()
    # #prints geme over
    # def game_over(self):
    #     #goes to the middle of the screen
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align=ALIGNMENT,font=FONT)

    #fn increases the score
    def increase_score(self):
        self.score +=1
        self.clear() #deletes the object with the score
        self.update_scoreboard() #gives the new score

