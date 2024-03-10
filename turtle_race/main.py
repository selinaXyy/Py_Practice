import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

NUM_OF_TURTLES = 6
race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color:")
colors = ["red", "orange", "gold", "green", "blue", "purple"]
turtles = []
winner = None
x = -230
y = -100

def create_turtles():
    global y
    for num in range(NUM_OF_TURTLES):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[num])
        new_turtle.setposition(x,y)
        turtles.append(new_turtle)
        y += 40

def check_bet(user_bet_par, winner_turtle_par):
    if user_bet_par == winner_turtle_par:
        print(f"You've won! The {winner_turtle_par} turtle is the winner!")
    else:
        print(f"You've lost! The {winner_turtle_par} turtle is the winner!")

if user_bet:
    race_on = True
    create_turtles()

while race_on and winner == None:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            winner = turtle.pencolor()

check_bet(user_bet, winner)

screen.exitonclick()