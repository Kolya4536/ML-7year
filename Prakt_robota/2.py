from turtle import *
a= int(input('Яка буде сторона квадрату?'))
b= a+20
color('red')
for i in range(2):
    fd(a)
    right(90)
    fd(a)
    right(90)


exitonclick()