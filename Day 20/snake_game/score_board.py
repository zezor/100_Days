from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Score (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        #self.write((0, 0), True)
        self.goto(x=0, y=270 )
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.color("white")
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
        self.hideturtle()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

