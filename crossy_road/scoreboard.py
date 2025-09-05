from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.level = 1
        self.write(f"Level {self.level}", align= "center", font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Level {self.level}", align= "center", font=FONT)


    def increase_level(self):
        self.level += 1
        self.update_score()
