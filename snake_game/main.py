from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # detect collision with turtle distance method
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    xcor = snake.head.xcor()
    ycor = snake.head.ycor()
    if xcor > (SCREEN_WIDTH / 2 - 20) or xcor < (-SCREEN_WIDTH/2) or ycor > (SCREEN_HEIGHT / 2 - 20) or ycor < (
            -SCREEN_HEIGHT / 2):
        scoreboard.reset()
        snake.reset_snake()

    # detect collision with tail
    # if head collides with any segment in the tail trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()
