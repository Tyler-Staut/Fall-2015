#Author: Tyler R. Staut
#File Name: Lab Assignment 10
#Date: 9/14/2015
#Description: TURTLE MAYHEM!!!!

#----------IMPORTS----------
import turtle
#---------------------------

#----------INPUT------------
radius = int(input("Type in a radius between 0 and 10 for your circles: ")) * 10
#---------------------------

#---------------DEFINING TURTLES---------------
#Created the 4 turtle definitions so that I can call them later instead of writing them out one by one.
def turtleOne():
    Beans = turtle.Turtle()     #Decided to name all of my turtles because I can.
    Beans.hideturtle()          #To hide the Turtle
    Beans.shape("turtle")       #Decided to make their shape appropriate to the module even though it is not shown
    Beans.speed(0)      #To prevent lines in the center
    Beans.pensize(1)
    Beans.penup()
    Beans.left(0)       #Have this to start the first turtle 0 degrees out of phase
    Beans.forward(radius)
    Beans.pendown()
    Beans.circle(radius)        #Draws a circle here
    
def turtleTwo():
    Beanie = turtle.Turtle()
    Beanie.hideturtle()
    Beanie.shape("turtle")
    Beanie.speed(0)
    Beanie.pensize(1)
    Beanie.penup()
    Beanie.left(90)     #Have this to start the second turtle 90 degrees out of phase
    Beanie.forward(radius)
    Beanie.pendown()
    Beanie.circle(radius)       #Draws a circle here
    
    
def turtleThree():
    NeverForget = turtle.Turtle()
    NeverForget.hideturtle()
    NeverForget.shape("turtle")
    NeverForget.speed(0)
    NeverForget.pensize(1)
    NeverForget.penup()
    NeverForget.left(180)   #Have this to start the third turtle 180 degrees out of phase
    NeverForget.forward(radius)
    NeverForget.pendown()
    NeverForget.circle(radius)      #Draws a circle here
    
    
def turtleFour():
    FreshPrince = turtle.Turtle()
    FreshPrince.hideturtle()
    FreshPrince.shape("turtle")
    FreshPrince.speed(0)
    FreshPrince.pensize(1)
    FreshPrince.penup()
    FreshPrince.left(270)   #Have this to start the fourth turtle 270 degrees out of phase
    FreshPrince.forward(radius)
    FreshPrince.pendown()
    FreshPrince.circle(radius)      #Draws a circle here
#----------------------------------------
    

#----------USED TO RUN THE TURTLES----------
turtle.title("The 4 Amazing Circles!!!")    #Decided to title the window just so I can try the features.

turtleOne()

turtleTwo()

turtleThree()

turtleFour()
#-------------------------------------------

#----------RADIUS TURTLE----------
Rad = turtle.Turtle()
Rad.hideturtle()
Rad.penup()
Rad.forward(radius)
Rad.right(90)
Rad.forward(radius)

#Creates the central point on the bottom right circle
Rad.dot(5)

#Writes the radius
Rad.write("Your Radius is %d" % (radius/10),
          font=("Arial", 12,
                "normal"))
#To create the dashed line to show the radius
Rad.left(90)
for i in range(5): 
    Rad.forward(radius/10)
    Rad.penup()
    Rad.forward(radius/10)
    Rad.pendown()
#---------------------------------

#Ends the loop to keep the turtle window thing on screen.
turtle.mainloop()
