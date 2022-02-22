import turtle
import random

screen = turtle.Screen()
screen.title('Turtle livestream')
screen.mode("logo")
turtle.bgcolor('#238931')

ziggy = turtle.Turtle()
box = ziggy.clone()
box.speed(0)
ziggy.penup()
ziggy.shape("turtle")
ziggy.speed(0)
ziggy.fillcolor('blue')
ziggy.goto(-50, 0)
ziggy.pencolor('pink')
x = False

box.penup()
box.ht()
box.goto(-100, 150)
box.pendown()
box.color('#1BE4C8')
box.begin_fill()
box.circle(50)
box.end_fill()

box.width(5)
box.color('black')
box.penup()
box.ht()
box.goto(-220, -220)
box.pendown()
b = 0
for i in range(4):
    box.fd(440)
    box.rt(90)
    b += 1

box.penup()
box.goto(200, 190)
box.pendown()
box.color('light grey')
box.begin_fill()
box.circle(15)
box.end_fill()

box.penup()
box.goto(205, 175)
box.pendown()
box.width(2)
box.begin_fill()
box.circle(4)
box.end_fill()

box.penup()
box.goto(170, 200)
box.pendown()
box.width(2)
box.begin_fill()
box.circle(6)
box.end_fill()

box.width(5)
box.color('brown')
box.penup()
box.ht()
box.goto(-130, -150)
box.pendown()

box.begin_fill()

box.lt(27)
for i in range(2):
    box.fd(50)
    box.rt(90)
    box.fd(10)
    box.rt(90)

box.end_fill()

c = True

while x is False:
    while c is True:
        for i in range(5):
            ziggy.rt(50)
            ziggy.fd(20)
            ziggy.lt(100)
            ziggy.fd(20)
            ziggy.rt(50)
        ziggy.rt(90)
        c = False

    for i in range(46):

        ziggy.rt(50)
        ziggy.fd(20)
        ziggy.stamp()
        if c is False:
            ziggy.clearstamps(1)

        ziggy.lt(100)
        ziggy.fd(20)
        ziggy.stamp()
        ziggy.rt(50)

        if c is False:
            ziggy.clearstamps(1)

        if i == 8:
            ziggy.rt(130)
        elif i == 22:
            ziggy.lt(130)
        elif i == 31:
            ziggy.lt(130)
        elif i == 45:
            ziggy.rt(130)
