import turtle
turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(90)
t.pensize(3)
for i in range(25):
    t.pencolor("red")
    t.circle(15)
    t.pencolor("yellow")
    t.right(20)
    for j in range(5):
        t.pencolor('gold')
        t.fd(113)
        t.pencolor("gold")
        t.right(143)
        t.pencolor("blue")
        t.circle(15+j)
t.penup()
t.fd(400)
t.lt(90)
t.pendown()
for i in range(25):
    t.pencolor("red")
    t.circle(15)
    t.pencolor("yellow")
    t.right(20)
    for j in range(5):
        t.pencolor('gold')
        t.fd(113)
        t.pencolor("gold")
        t.right(143)
        t.pencolor("blue")
t.penup()
t.fd(-400)
t.lt(90)
t.pendown()
for i in range(25):
    t.pencolor("red")
    t.circle(15)
    t.pencolor("yellow")
    t.right(20)
    for j in range(5):
        t.pencolor('gold')
        t.fd(113)
        t.pencolor("gold")
        t.right(143)
        t.pencolor("blue")
t.penup()
t.lt(90)        
t.fd(400)
t.pendown()
for i in range(25):
    t.pencolor("red")
    t.circle(15)
    t.pencolor("yellow")
    t.right(20)
    for j in range(5):
        t.pencolor('gold')
        t.fd(113)
        t.pencolor("gold")
        t.right(143)
        t.pencolor("blue")
             
turtle.done()