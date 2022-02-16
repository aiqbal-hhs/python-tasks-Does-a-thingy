import turtle
import random

screen = turtle.Screen()
screen.title('Turtle livestream')
screen.mode("logo")
turtle.bgcolor('green')

first = turtle.Turtle()
box = first.clone()
box.speed(11)
first.speed(random.randint(1, 3))
first.penup()
first.fillcolor('lightgreen')
first.shape("turtle")
second = first.clone()
x = False
fangle = first.towards(0, 0)
sangle = second.towards(0, 0)

box.penup()
box.ht()
box.goto(205, -185)
box.pendown()
box.color('#1BE4C8')
box.begin_fill()
for i in range(4):
    box.fd(370)
    box.circle(20, 90)
box.end_fill()

box.width(5)
box.color('black')
box.penup()
box.ht()
box.goto(-220, -220)
box.pendown()
for i in range(4):
    box.fd(440)
    box.rt(90)

box.penup()
box.goto(195, 185)
box.pendown()
box.color('light grey')
box.begin_fill()
box.circle(15)
box.end_fill()

box.penup()
box.goto(200, 170)
box.pendown()
box.width(2)
box.begin_fill()
box.circle(4)
box.end_fill()

box.penup()
box.goto(165, 195)
box.pendown()
box.width(2)
box.begin_fill()
box.circle(6)
box.end_fill()

box.width(5)
box.color('brown')
box.penup()
box.ht()
box.goto(-170, -200)
box.pendown()

box.begin_fill()

box.lt(27)
for i in range(2):
    box.fd(60)
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

first.lt(random.randint(0, 359))
second.lt(random.randint(0, 359))

b = 0

while x is False:
    # must find how to turn turtles around
    if first.xcor() >= 190:
        first.setx(180)
        fangle == first.towards(0, 0)
        first.lt(fangle)
        first.fd(5)
    elif first.xcor() <= -190:
        first.setx(-180)
        fangle == first.towards(0, 0)
        first.lt(fangle)
        first.fd(5)
        
    if first.ycor() >= 190:
        first.sety(180)
        fangle == first.towards(0, 0)
        first.lt(fangle)
        first.fd(5)
    elif first.ycor() <= -190:
        first.sety(-180)
        fangle == first.towards(0, 0)
        first.lt(fangle)
        first.fd(5)
        
    if second.xcor() >= 190:
        second.setx(180)
        sangle == second.towards(0, 0)
        second.lt(sangle)
        second.fd(5)
    elif second.xcor() <= -190:
        second.setx(-180)
        sangle == second.towards(0, 0)
        second.lt(sangle)
        second.fd(5)
        
    if second.ycor() >= 190:
        second.sety(180)
        sangle == second.towards(0, 0)
        second.lt(sangle)
        second.fd(5)
    elif second.ycor() <= -190:
        second.sety(-180)
        sangle == second.towards(0, 0)
        second.lt(sangle)
        second.fd(5)
    first.fd(random.randint(0, 6))
    first.lt(random.randint(-40, 40))
    first.speed(random.randint(1, 2))
    second.fd(random.randint(0, 8))
    second.lt(random.randint(-30, 30))
    second.speed(random.randint(1, 4))
