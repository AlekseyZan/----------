import turtle
 
turtlePen = turtle.Turtle()
window = turtle.Screen()
 
window.bgcolor("black")
 
 
def polygon(n, size=80):
    if n > 2:
        angle = 360 / n
 
        for n in range(0, n):
            turtlePen.left(angle)
            turtlePen.forward(size)
 
def polygon(n, size=50):
    if n > 2:
        angle = 360 / n
 
        for n in range(0, n):
            turtlePen.color(colors[n % 5])
            turtlePen.left(angle)
            turtlePen.forward(size) 
turtlePen.speed(100)
 
colors = ['orange', 'cyan', 'blue', 'green', 'red']
 
size = 25
 
for i in range(0, 100):
    turtlePen.color(colors[i % 5])
    polygon(4, size)
    turtlePen.left(5)
    size = size + 3
 
window.mainloop()