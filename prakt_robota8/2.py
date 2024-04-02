import turtle
from turtle import *
a = int(input(" Яка буде довжина сторони квадрата?"))
b = 10
c = 120
penup()
turtle.goto(-300,0)
hideturtle()
pendown()

for i in range(4):
    for i in range(4):
        fd(a)
        right(90)
    a = a + b
    penup()
    fd(c)
    pendown()
    c = c + b




exitonclick()
