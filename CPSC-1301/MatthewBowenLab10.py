# Author:       Matthew Newton Bowen
# Program Name: MatthewBowenLab10.py
# Date:         September 14, 2015
# Description: Playing with the Turtle

import turtle #imports the turtle module

radius = int(input("How large would you like the radius to be? ")) #gets input of radius

turtle.showturtle()                 #makes turtle visible
turtle.penup()                      #turtle will not draw
turtle.goto(radius, -radius)        #moves turtle to the coordinates of (x = radius, y = -radius)
turtle.pendown()                    #turtle will now draw
turtle.circle(radius)               #will draw a circle of radius inputed by user
turtle.penup()                      #turtle will not draw
turtle.goto(radius, radius)         #moves turtle to the coordinates of (x = radius, y = radius)
turtle.pendown()                    #turtle will draw
turtle.circle(radius)               #will draw a circle of radius inputed by user
turtle.penup()                      #turtle will not draw
turtle.goto(-radius, radius)        #moves turtle to the coordinates of (x = -radius, y = radius)
turtle.pendown()                    #turtle will draw
turtle.circle(radius)               #will draw a circle of radius inputed by user
turtle.penup()                      #turtle will not draw
turtle.goto(-radius, -radius)       #moves turtle to the coordinates of (x = -radius, y = -radius)
turtle.pendown()                    #turtle will draw
turtle.circle(radius)               #will draw a circle of radius inputed by user
turtle.penup()                      #turtle will not draw
turtle.goto((2*radius), 0)          #moves turtle to the coordinates of (x = 2*radius, y = 0)
turtle.left(180)                    #rotates turtle 180 degrees
turtle.pendown()                    #turtle will draw
turtle.forward(radius)              #turtle moves forward the number of units defined by radius
turtle.write(("radius = %d") % (radius))    #writes 
turtle.mainloop()                   #ends program so turtle will remain on screen