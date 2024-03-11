from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

#user_1 (right)
paddle_1 = Paddle((350, 0))
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")

#user_2 (left)
paddle_2 = Paddle((-350, 0))
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")

#ball
ball = Ball()

#score_board
score_board = ScoreBoard()

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()
    #bounces the ball if detected collision with wall (only modifies y axis)
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    #if users catched the ball (only modifies x axis)
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #if user_1(right) didn't catch the ball (reset && ball goes back to center)
    if ball.xcor() > 360:
        ball.reset()
        score_board.user_2_scored()

    #if user_2(left) didn't catch the ball
    if ball.xcor() < -360:
        ball.reset()
        score_board.user_1_scored()

screen.exitonclick()