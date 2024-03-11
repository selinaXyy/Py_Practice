from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.user_1_score = 0
        self.user_2_score = 0
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.user_1_score, align="center", font=("Courier", 80, "normal"))
        self.goto(-100, 200)
        self.write(self.user_2_score, align="center", font=("Courier", 80, "normal"))

    def user_1_scored(self):
         self.user_1_score += 1
         self.update_score_board()

    def user_2_scored(self):
         self.user_2_score += 1
         self.update_score_board()