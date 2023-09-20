import turtle

# Create a turtle object
emoji = turtle.Turtle()
emoji.shape("turtle")

# Set the pen color and fill color for the emoji
emoji.pencolor("black")
emoji.fillcolor("red")

# Draw the rover body (a red rectangle)
emoji.begin_fill()
emoji.forward(100)
emoji.left(90)
emoji.forward(50)
emoji.left(90)
emoji.forward(100)
emoji.left(90)
emoji.forward(50)
emoji.end_fill()

# Set the pen color and fill color for the wheels
emoji.pencolor("black")
emoji.fillcolor("gray")

# Draw the left wheel (a gray circle)
emoji.penup()
emoji.goto(25, -25)
emoji.pendown()
emoji.begin_fill()
emoji.circle(20)
emoji.end_fill()

# Draw the right wheel (a gray circle)
emoji.penup()
emoji.goto(75, -25)
emoji.pendown()
emoji.begin_fill()
emoji.circle(20)
emoji.end_fill()

# Set the pen color for the camera
emoji.pencolor("black")

# Draw the camera mast (a vertical line)
emoji.penup()
emoji.goto(50, 0)
emoji.pendown()
emoji.forward(30)

# Draw the camera (a small rectangle)
emoji.penup()
emoji.goto(40, 30)
emoji.pendown()
emoji.forward(20)
emoji.right(90)
emoji.forward(10)
emoji.right(90)
emoji.forward(20)
emoji.right(90)
emoji.forward(10)

# Hide the turtle
emoji.hideturtle()

# Keep the turtle graphics window open until manually closed
turtle.done()
