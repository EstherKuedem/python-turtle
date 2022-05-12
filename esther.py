import turtle
import turtle as t
t.speed(0)
win = turtle.Screen()
win.bgcolor("white")
t.width(2)

t.pencolor("purple")
t.color("black")
t.begin_fill()
t.circle(220)
t.end_fill()
t.up()
t.goto(40,370)
t.pendown()

t.color("blue")
t.begin_fill()
t.lt(180)
t.fd(200)
t.lt(90)
t.fd(300)
t.lt(90)
t.fd(310)
t.lt(90)
t.fd(300)
t.lt(90)
t.fd(200)
t.end_fill()


t.goto(-5,373)
t.color("red")
t.begin_fill()
t.circle(150)
t.end_fill()


t.goto(98,120)
t.color("yellow")
t.begin_fill()
for k in range(4):
    t.fd(210)
    t.rt(90)
t.end_fill()


t.up()
t.goto(-5,325)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(100)
t.end_fill()



t.goto(60,165)
t.color("blue")
t.begin_fill()
for k in range(4):
    t.fd(130)
    t.rt(90)
t.end_fill()


t.goto(-5,290)
t.color("red")
t.begin_fill()
t.circle(60)
t.end_fill()




t.goto(30,195)
t.color("yellow")
t.begin_fill()
for k in range(4):
    t.fd(75)
    t.rt(90)
t.end_fill()

t.goto(-7,265)
t.color("black")
t.begin_fill()
t.circle(35)
t.end_fill()



t.goto(15,210)
t.color("blue")
t.begin_fill()
for k in range(4):
    t.fd(46)
    t.rt(90)
t.end_fill()


t.ht()
