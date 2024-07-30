from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong-Game")
screen.tracer(0)


r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")


ball = Ball(0, 0)
scoreboard = Scoreboard()


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with upper and lower walls
    if ball.ycor() > 288 or ball.ycor() < -288:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 328 or ball.distance(l_paddle) < 50 and ball.xcor() < -328:
        ball.bounce_x()

    # r_padel misses
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    # l_padel misses
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()


screen.exitonclick()
