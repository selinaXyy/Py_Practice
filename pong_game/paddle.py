from turtle import Turtle

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
        if y <= 240:
            self.sety(y + 20)

    def go_down(self):
        y = self.ycor()
        if y >= -240:
            self.sety(y - 20)
