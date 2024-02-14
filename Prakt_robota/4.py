from turtle import *
a= int(input('Яка буде сторона  квадрату?'))
b= a-20
color('blue')
width(3)
for i in range(4):
    fd(a)
    right(90)
penup()
fd(a+20)
pendown()
color('red')
for i in range(4):
    fd(b)
    right(90)
exitonclick()