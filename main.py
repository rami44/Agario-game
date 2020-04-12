from turtle import *

class Ball(Turtle):
    def __init__(self, x, y, dx, dy, r, color):
        Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.color(color)
        self.size = r/10
        self.shapesize(r/10)
        self.goto(x,y)

    def move(self, screen_width, screen_height):
        current_x = self.xcor()
        new_x = (current_x + self.dx)
        current_y = self.ycor()
        new_y = (current_y + self.dy)
        right_side_ball = (new_x + self.r)
        left_side_ball = (new_x - self.r)
        top_side_ball = (new_y + self.r)
        bottom_side_ball = (new_y - self.r)
        self.goto(new_x, new_y)
        if right_side_ball >= screen_width or left_side_ball <= -screen_width:
            self.dx = -self.dx
        if top_side_ball >= screen_height or bottom_side_ball <= -screen_height:
            self.dy = -self.dy

    def new_Ball(self, x, y, dx, dy, r, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.color(color)
        self.shapesize(r/10)
        self.goto(x,y)















