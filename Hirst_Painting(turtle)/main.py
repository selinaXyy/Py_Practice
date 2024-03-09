import colorgram
import random
from turtle import Turtle, Screen, colormode

selina = Turtle()
selina.hideturtle()
selina.speed("fastest")
colormode(255)
selina.penup()
colors = colorgram.extract('sample.jpeg', 10) #returns a list

CIRCLE_RADIUS = 10
GAP_BETWEEN = 50

def set_position(x_cor, y_cor):
    selina.setx(x_cor)
    selina.sety(y_cor)

def set_rand_color():
    rand_color_index = random.randint(0, len(colors) - 1)
    rgb = colors[rand_color_index].rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    selina.pencolor(r, g, b)
    selina.fillcolor(r, g, b)

def draw_and_fill_circle():
    selina.begin_fill()
    selina.circle(CIRCLE_RADIUS)
    selina.end_fill()

def paint(side_num):
    for row in range(side_num):
        for column in range(side_num):
            set_rand_color()
            selina.pendown()
            draw_and_fill_circle()
            selina.penup()
            selina.forward(GAP_BETWEEN)
        
        set_position(-230, selina.ycor() + GAP_BETWEEN)

#set starting position
set_position(-230, -240)
paint(10)

screen = Screen()
screen.exitonclick()