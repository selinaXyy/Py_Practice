from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBord
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0) #turn off tracer

snake = Snake()
food = Food()
score_board = ScoreBord()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.snake_head.distance(food) < 20: #food is 10*10
        snake.extend()
        food.refresh()
        score_board.increment_score()

    #detect collision with wall
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        score_board.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()