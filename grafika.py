from turtle import*
t = Turtle()
t.screen.setup(800,800)
t.screen.bgcolor("yellow")
t.up()
t.goto(0,40)
t.color("green")
t.write("Оленька!",move = False,align="center",font=("Helvetica",25,"bold italic"))
t.up()
t.goto(40,0)
t.color("red")
t.write("Я ТЕБЯ ЛЮБЛЮ !",move=True,align="center",font = ("Helvetica",20,"bold"))


my_turtle_cursor =Turtle()

def pause():
    my_turtle_cursor.speed(2)
    for i in range(40):
        my_turtle_cursor.lt(90)
def write_I_inside_heart():
    my_turtle_cursor.penup()
    my_turtle_cursor.goto(-240,15)
    my_turtle_cursor.pencolor('#00FFFF')
    my_turtle_cursor.write('Я',font = ('Helevetica',33,'bold'))
def write_love_inside_heart():
    my_turtle_cursor.penup()
    my_turtle_cursor.goto(-160,15)
    my_turtle_cursor.pencolor('#00FFFF')
    my_turtle_cursor.write('ТЕБЯ',font = ('Helevetica',33,'bold'))
def write_you_inside_heart():
    my_turtle_cursor.penup()
    my_turtle_cursor.goto(40,15)
    my_turtle_cursor.pencolor('#00FFFF')
    my_turtle_cursor.write('ЛЮБЛЮ',font = ('Helevetica',33,'bold'))
def draw_complete_heart():
    my_turtle_cursor.fillcolor('#FF0000')
    my_turtle_cursor.begin_fill()
    my_turtle_cursor.lt(140)
    my_turtle_cursor.fd(294)
    draw_lt_curve_of_heart()
    my_turtle_cursor.right(190)
    draw_right_curve_of_heart()
    my_turtle_cursor.fd(294)
    my_turtle_cursor.end_fill()
def draw_lt_curve_of_heart():
    my_turtle_cursor.speed(40)
    for i in range(440):
        my_turtle_cursor.right(0.5)
        my_turtle_cursor.fd(1.2)
def draw_right_curve_of_heart():
    my_turtle_cursor.speed(40)
    for i in range(440):
        my_turtle_cursor.right(0.5)
        my_turtle_cursor.fd(1.2)
my_turtle_cursor.penup()
my_turtle_cursor.goto(0,-200)
my_turtle_cursor.pendown()
my_turtle_cursor.speed(40)
draw_complete_heart()
write_I_inside_heart()
write_love_inside_heart()
write_you_inside_heart()
#turtle.done()


t.screen.exitonclick()
t.screen.mainloop()