from turtle import Turtle

TEXT_ALIGN = "center"
TEXT_FONT = ("Courier", 24, "normal")

class ScoreBord(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt") as data:
            self.high_score = int(data.read()) #retrives high score form data.txt

        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_score()

    def increment_score(self):
        self.score += 1
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=TEXT_ALIGN, font=TEXT_FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}") #rewrite high score in data.txt

        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=TEXT_ALIGN, font=TEXT_FONT)