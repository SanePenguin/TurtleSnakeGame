from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen_size = (800, 800)
screen.setup(width=screen_size[0], height=screen_size[1])
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

food = Food(screen_size)
scoreboard = Scoreboard(height=screen_size[0]//2 -40)

DIFFICULTIES = {"Sonic": 0.04, "Hard": 0.07, "Normal": 0.1, "Easy": 0.15, "Baby": 0.2}
SPEED = DIFFICULTIES["Hard"]
game_is_on = True
while game_is_on:
    screen.update()

    snake.move()
    time.sleep(SPEED)
    #Detect Collison with food
    if snake.head.distance(food) < 15:
        food.spawn_random(screen_size[0], screen_size[1])
        snake.grow()
        scoreboard.increase_score()

    #Detect Collosion with wall
    if snake.head.xcor() > screen_size[0]//2 - 20 or snake.head.xcor() < -(screen_size[0]//2) or snake.head.ycor() > screen_size[1]//2 or snake.head.ycor() < -(screen_size[1]//2):
        game_is_on = False
        scoreboard.game_over()

    #Detect Collision with tail
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    
screen.exitonclick()
