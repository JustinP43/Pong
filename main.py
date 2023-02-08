from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-380,0))
r_paddle = Paddle((380,0))
scoreboard = Scoreboard()

ball = Ball()

screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(l_paddle.move_down,"s")
screen.onkey(r_paddle.move_down,"Down")

screen.update()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with top and bottom boundary
    if ball.ycor() >= 285 or ball.ycor() < -285:
        ball.bounce()

    #Detect collision with paddles
    if (ball.distance(l_paddle) < 50 and ball.xcor() < -350) or (ball.distance(r_paddle) < 50 and ball.xcor() > 350):
        ball.pong()
    
    #Detect a miss by left paddle
    if ball.xcor() < -380:
        scoreboard.right_point()
        ball.reset_position()        
    #Detect a miss by right paddle
    if ball.xcor() > 380:
        scoreboard.left_point()
        ball.reset_position()
    


screen.exitonclick()

