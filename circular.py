import turtle
import turtle as t
win = turtle.Screen()
win.bgcolor("yellow")
t.speed(0)
t.color("black")
t.begin_fill()
t.circle(200)
t.up()
t.end_fill()

t.color("blue")
t.begin_fill()
t.goto(0,45)
t.pd()
t.circle(150)
t.up()
t.end_fill()


t.color("red")
t.begin_fill()
t.goto(0,95)
t.pd()
t.circle(100)
t.up()
t.end_fill()


t.color("yellow")
t.begin_fill()
t.goto(0,140)
t.pd()
t.circle(50)
t.end_fill()

t.ht()
