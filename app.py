import turtle
import time
import random
import math
from main import Ball 


turtle.colormode(255)
turtle.tracer(0)
turtle.hideturtle()
running = True
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

my_ball = Ball(0,0,10,15,20, (random.randint(0,225), random.randint(0,225), random.randint(0,225)))

number_of_balls = 6
minimum_ball_radius = 5
maximum_ball_radius = 50
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5

BALLS = []

for i in range(number_of_balls):
    x = random.randint(-screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
    y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
    dx = random.randint(minimum_ball_dx, maximum_ball_dx)
    while (dx == 0):
        dx = random.randint(minimum_ball_dx, maximum_ball_dx)
  
    dy = random.randint(minimum_ball_dy, maximum_ball_dy)
    while (dy == 0):
        dy = random.randint(minimum_ball_dy, maximum_ball_dy)

    r = random.randint(minimum_ball_radius, maximum_ball_radius)
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    print(color)
    new_ball = Ball( x, y, dx, dy, r, color)
    BALLS.append(new_ball)

##part_2
def move_all_balls():
    for ball in BALLS:
        ball.move(screen_width,screen_height)

##part_3

def collide(ball_a, ball_b):
    if ball_a == ball_b:
        return False
    if ball_a.r + ball_b.r >= ((ball_a.xcor() - ball_b.xcor())**2 + (ball_a.ycor() - ball_b.ycor())**2)**.5 :       
       return True
    else :
        return False 

##part_4

def check_all_balls_collisions():
    print('collision here')
    global running
    all_balls=[]
    all_balls.append(my_ball)
    for ball in BALLS:
        all_balls.append(ball)
    for ball_a in all_balls:
        for ball_b in all_balls:
            
            if collide(ball_a, ball_b):
                

                X = random.randint(-screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
                y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
                dx = random.randint(minimum_ball_dx, maximum_ball_dx)
                while (dx == 0):
                    dx = random.randint(minimum_ball_dx, maximum_ball_dx)
              
                dy = random.randint(minimum_ball_dy, maximum_ball_dy)
                while (dy == 0):
                    dy = random.randint(minimum_ball_dy, maximum_ball_dy)

                r = random.randint(minimum_ball_radius, maximum_ball_radius)
                color = (random.randint(0,255)
                         , random.randint(0,255), random.randint(0,255))
                if ball_a.r < ball_b.r :
                    ball_a.new_Ball(x,y,dx,dy,r,color)
                    ball_b.r += 5
                    ball_b.shapesize(ball_b.r/10)

                    if my_ball == ball_a :
                        running = False
                        print("game over")

                        
                        
                        
                if ball_a.r > ball_b.r :
                    ball_b.new_Ball(x,y,dx,dy,r,color)
                    ball_a.r += 5
                    ball_a.shapesize(ball_a.r/10)
                    if my_ball == ball_b :
                        running = False
                        print("game over")
                        break
                        
                      
##part_5
                        
                        
def movearound():
    x=turtle.getcanvas().winfo_pointerx() - screen_width * 2
    y= screen_height * 1.4 - turtle.getcanvas().winfo_pointery()
    my_ball.goto(x,y)


##part_6


while running == True :
    screen_width = turtle.getcanvas().winfo_width()/2
    screen_height = turtle.getcanvas().winfo_height()/2
    print('here')
    movearound() 
    move_all_balls()
    check_all_balls_collisions()

    turtle.update()
    time.sleep(.1)

    if my_ball.r >= 150 :
        running = False
        turtle.write("YOU WIN", move=False, align="center", font=("Times New Roman", 100 , "normal"))
        turtle.write("your score: " + str(my_ball.r),move=False, align="center", font=("Arial", 15 , "normal"))


if my_ball.r<150:
    turtle.write("YOU LOST",move=False, align="center", font=("Times New Roman", 100 , "normal"))
    turtle.write("your score: " + str(my_ball.r),move=False, align="center", font=("Arial", 15 , "normal"))

turtle.mainloop()





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




   











