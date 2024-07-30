from turtle import Turtle

UP = 90
DOWN = 270


class Ball(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(xcor, ycor)
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 0.005

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= .8

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.005
        self.bounce_x()
