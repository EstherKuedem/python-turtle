
import turtle
t = turtle.Pen()
# drawing the right eye
t.up()
t.goto(150, 150)
t.pd()
t.begin_fill()
t.circle(50)
t.end_fill()
t.speed(0)

#drawing the left eye
t.up()
t.goto(-150, 150)
t.pd()
t.begin_fill()
t.circle(50)
t.end_fill()

#drawing the nosse
t.up()
t.goto(10, 100)
t.pd()
t.rt(60)
t.fd(150)
t.rt(120)
t.fd(150)
t.rt(120)
t.fd(150)

#drawing the mouth
t.up()
t.goto(-150, -150)
t.setheading(0)
t.pd()
for k in range(2):
    t.fd(300)
    t.rt(90)
    
    t.fd(100)
    t.rt(90)

t.width(4)    
t.up()
t.goto(-200,-300)
t.pd()
t.fd(400)

t.ht()
turtle.mainloop()




