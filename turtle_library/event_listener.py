from turtle import Turtle, Screen

selina = Turtle()

def move_forward():
    selina.forward(10)

def move_backward():
    selina.backward(10)

def turn_right():
    selina.setheading(selina.heading() - 10)

def turn_left():
    selina.setheading(selina.heading() + 10)

def clear_canvas():
    screen.reset()

screen = Screen()
screen.listen()

screen.onkey(key="w", fun=move_forward) #call back
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_canvas)

screen.exitonclick()