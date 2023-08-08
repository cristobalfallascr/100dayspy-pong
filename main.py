from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)


    snake.move()

    if snake.head.distance(food) < 15:
        print('nom nom')
        scoreboard.increase_score()
        snake.extend_snake()
        food.refresh()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:

       scoreboard.reset()
       snake.reset_snake()
       snake.move()
    for body_part in snake.snake_body[1:]:

        if snake.head.distance(body_part) < 10:
            scoreboard.reset()
            snake.reset_snake()
            snake.move()

screen.exitonclick()