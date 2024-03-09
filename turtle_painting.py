from turtle import *
from random import randint, choice

selina = Turtle()
mode("standard")
selina.shape("turtle")
selina.color("DarkTurquoise")
colormode(255)

# draw dashed-line circle
# for _ in range(50):
#     selina.pendown()
#     selina.forward(5)
#     selina.penup()
#     selina.forward(5)
#     selina.left(8)

################################################################

#draw triangle --> decagon
def change_pencolor():
    selina.pencolor(randint(0,255),randint(0,255),randint(0,255))

# def draw_shape(side_num):
#     for side in range(side_num):
#         selina.forward(100)
#         selina.right(360 / side_num)

# for angles in range(3, 11):
#     draw_shape(angles)
#     change_pencolor()

################################################################

#draw 'random walk'
# selina.pensize(7)
selina.speed("fastest")
# def rand_direction():
#     direction = [0, 90, 180, 270] #[east, north, west, south] --> standard
#     selina.setheading(choice(direction))

# for step in range(500):
#     change_pencolor()
#     rand_direction()
#     selina.forward(30)

################################################################

#draw 'spirograph'
# def draw_spirograph(degrees_of_gap):
#     for gap in range(int(360 / degrees_of_gap)):
#         change_pencolor()
#         selina.circle(100)
#         selina.setheading(selina.heading() + degrees_of_gap)

# draw_spirograph(5)

################################################################

screen = Screen()
screen.exitonclick()