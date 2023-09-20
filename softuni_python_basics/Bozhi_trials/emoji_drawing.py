import turtle
bozhi = turtle.Turtle()
bozhi.shape("turtle")

bozhi.pendown()
bozhi.pencolor("orange")
bozhi.fillcolor("orange")

#drawing the emoji circle
bozhi.begin_fill()
bozhi.circle(100)
bozhi.end_fill()


bozhi.pencolor("black")
bozhi.pensize(5)

#drawing left eye
bozhi.penup()
bozhi.goto(-50, 140)
bozhi.pendown()
bozhi.right(40)
bozhi.forward(20)
bozhi.right(100)
bozhi.forward(20)

#drawing right eye
bozhi.penup()
bozhi.goto(50, 140)
bozhi.pendown()
bozhi.left(0)
bozhi.forward(20)
bozhi.left(100)
bozhi.forward(20)

#left eye brow
bozhi.penup()
bozhi.goto(-60, 160)
bozhi.pendown()
bozhi.pensize(3)
bozhi.circle(15, 110)

#right eye brow
bozhi.penup()
bozhi.goto(60, 175)
bozhi.pendown()
bozhi.pensize(3)
bozhi.circle(15, -110)

#draw mouth
bozhi.penup()
bozhi.goto(30, 60)
bozhi.pendown()
bozhi.pensize(5)
bozhi.circle(-50, -90)

turtle.done()
