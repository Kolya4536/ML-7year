from turtle import *
up()
goto(-350,0)
a=20
while a <= 200:
    down()
    for i in range(4):
        fd(a)
        right(90)
    up()
    fd(a+10)
    a += 20