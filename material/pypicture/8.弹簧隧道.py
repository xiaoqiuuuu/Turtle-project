import turtle as t
import random

t.speed(0)
t.hideturtle()
t.bgcolor('black')

i = 0
while i < 180:
    t.pencolor('cyan')
    t.penup()
    t.goto(0, 0)
    t.forward(200)
    t.pendown()
    t.circle(100)
    t.left(2)
    i += 1
t.done()
