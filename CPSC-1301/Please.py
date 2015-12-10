import turtle

turtle.left(180)
for x in range(180):
    turtle.forward(1)
    turtle.right(1)
turtle.right(90)
turtle.forward(20)
turtle.penup()
turtle.forward(95)
turtle.pendown()
turtle.right(180)
turtle.forward(15)

turtle.left(90)
for x in range(180):
    turtle.forward(.75)
    turtle.right(1)

turtle.mainloop()