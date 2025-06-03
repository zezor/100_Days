from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        #self.write((0, 0), True)
        self.goto(x=0, y=270 )
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.score} High Score {self.high_score}", align=ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.color("white")
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
    #     self.hideturtle()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

