from turtle import Turtle

class Score (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write(f"Score:, {self.score}", align="center", font=("Arial",10, "normal"))
        #self.write((0, 0), True)
        self.goto(x=0, y=270 )
        self.color("white")