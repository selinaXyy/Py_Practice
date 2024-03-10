from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__() #inherits features from the Turtle class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5) #normal size: 20*20
        self.color("yellow")
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        self.goto(x=randint(-280,280),y=randint(-280,280))