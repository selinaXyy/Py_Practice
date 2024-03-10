from turtle import Turtle

TEXT_ALIGN = "center"
TEXT_FONT = ("Courier", 24, "normal")

class ScoreBord(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_score()

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_score()
    
    def update_score(self):
        self.write(arg=f"Score: {self.score}", align=TEXT_ALIGN, font=TEXT_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=TEXT_ALIGN, font=TEXT_FONT)