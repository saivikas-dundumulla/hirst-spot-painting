from random import randint
import turtle
from turtle import Screen

timmy = turtle.Turtle()
screen = Screen()
turtle.colormode(255)

def random_color():
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    return (r, g, b)


screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
def draw_row():
    for i in range(10):
        timmy.dot(20, random_color())
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
def next_line(no_dots, gap):
    timmy.up()
    timmy.left(90)
    timmy.forward(gap)
    timmy.setheading(0)
    distance = no_dots*gap
    timmy.back(distance)
    timmy.down()
timmy.speed("fastest")
timmy.hideturtle()
for _ in range(10):
    draw_row()
    next_line(10, 50)


screen.exitonclick()