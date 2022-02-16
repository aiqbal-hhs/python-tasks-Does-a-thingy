import turtle
import random

screen = turtle.Screen()
screen.title('Turtle livestream')
screen.mode("logo")
turtle.bgcolor('#238931')

first = turtle.Turtle()
box = first.clone()
box.speed(11)
first.speed(random.randint(1, 3))
first.penup()
first.fillcolor('#38C74B')
first.shape("turtle")
second = first.clone()
ziggy = first.clone()
ziggy.speed(0)
ziggy.fillcolor('blue')
ziggy.goto(-50, 0)
ziggy.pencolor('pink')
x = False
fangle = first.towards(0, 0)
sangle = second.towards(0, 0)
zangle = ziggy.towards(220, 150)

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

# navigation is pick random
# can you use turtle.Turtle() to control all of the turtles?
# increase and decrease the number of turtles
# make senary?, write on the screen?,
# senary - most is pond, add log, add rock/s
# make player involved -> choose attributes -> 
c = True

first.lt(random.randint(0, 359))
second.lt(random.randint(0, 359))

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
        if i >= 7:
            ziggy.clearstamps(1)
        ziggy.lt(100)
        ziggy.fd(20)
        ziggy.stamp()
        if i >= 7:
            ziggy.clearstamps(1)
        ziggy.rt(50)
        
        if i == 8:
            ziggy.rt(130)
        elif i == 22:
            ziggy.lt(130)
        elif i == 31:
            ziggy.lt(130)
        elif i == 45:
            ziggy.rt(130)
    
    
