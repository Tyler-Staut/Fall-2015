import turtle
turtle.showturtle()
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.circle(100)
xcor=turtle.numinput("User Input","Enter x coordinate")
ycor=turtle.numinput("User Input","Enter y coordinate")
turtle.goto(xcor,ycor) 
