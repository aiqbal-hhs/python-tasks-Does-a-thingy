import turtle
frank = turtle.Turtle()
frank.speed(0)
frank.color('blue')

for i in range(100):
    frank.fd(184)
    frank.lt(27)
    frank.fd(10)
    frank.lt(74)

    
for i in range(120):
    #Change colors
    if i == 20:
        frank.color('red')
    elif i == 40:
        frank.color('orange')
    elif i == 60:
        frank.color('yellow')
    elif i == 80:
        frank.color('green')
    elif i == 100:
        frank.color('pink')
    #Draw the spirograph
    frank.forward(200)
    frank.left(184)
    frank.forward(40)
    frank.right(30)
