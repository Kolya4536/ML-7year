import turtle
from turtle import*
showturtle()
def move_right():
    setheading(0)
    fd(10)
    if xcor() < -0:
        turtle.color("red")
    if xcor() > 0:
        turtle.color("blue")
    if xcor() > 300:
        hideturtle()
        speed(0)
        setx(-300)
        showturtle()
        speed(1)

shape("turtle")
onkey(move_right,"Right")
listen()
exitonclick()