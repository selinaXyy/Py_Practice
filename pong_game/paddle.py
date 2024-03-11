from turtle import Turtle

STEP_SIZE = 20
Y_MAX = 240
Y_MIN = -240

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(position)
        self.speed("fastest")

    def go_up(self):
        y = self.ycor()
        if y <= Y_MAX:
            self.sety(y + STEP_SIZE)

    def go_down(self):
        y = self.ycor()
        if y >= Y_MIN:
            self.sety(y - STEP_SIZE)