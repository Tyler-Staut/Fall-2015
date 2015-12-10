#Author: Tyler R. Staut
#File Name: Lab Assignment 7
#Date: 9/2/2015
#Description: Floor Plan Program Thing that calculates total area of the floor

import math
import turtle


#------------------PLACE HOLDER----------------------
print('''\n         -----------\------------------/\n
        |          |  \             /\n
      W |     1    |  2 \ T<-or->T/\n
        |          |     /\-----/\n
        ----------------/--A\ /\n  ''')
print('''          
        |          |        |\n
      X |    3     |    4   |\n
        |          |        |\n
        -----Y----------Z----\n''')

#----------------------------------------------------

#-------------------BASE CODE------------------------

W = float(input("W: "))     #Input for Length of W   Used Float so if there is a room with a non-integer length
X = float(input("X: "))     #Input for Length of X
Y = float(input("Y: "))     #Input for Length of Y
Z = float(input("Z: "))     #Input for Length of Z
T = float(math.sqrt(W**2 + Z**2))
A = float(math.asin(W/T))

room1 = (W*Y)        #Coordinate system to equate room 1's area
room2 = (float((Z*T*math.sin(A)/2)))    #Coordinate system to equate room 2's area since it is a triangle
room3 = (X*Y)        #Coordinate system to equate room 3's area
room4 = (X*Z)        #Coordinate system to equate room 4's area

sq_foot_h = room1 + room3 + room4 + room2       #Calculates Square Footage of the House
sq_foot_c = room2 + room3                       #Caculated Square Footage for the rugs in room 2 and 3

print("Total square footage of the house:", sq_foot_h, "sq ft")             #Prints value for Total Square Footage of House
print("Total square footage of new carpet needed:", sq_foot_c, "sq ft")     #Prints value for Total Square Footage of Rugs

#----------------------------------------------------

#---------------------TURTLE-------------------------

wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Floor Plan")

Beans = turtle.Turtle()

Beans.color("black")
Beans.pensize(5)

Beans.forward(Z)
Beans.left(180-(A*(180/math.pi)))
Beans.forward(T)
Beans.left(A*(180/math.pi))
Beans.forward(Y)
Beans.left(90)
Beans.forward(W)
Beans.left(90)
Beans.forward(Y)
Beans.left(90)
Beans.forward(W)
Beans.left(180)
Beans.forward(W+X)
Beans.left(90)
Beans.forward(Z)
Beans.left(90)
Beans.forward(X)
Beans.left(90)
Beans.forward(Y+Z)
Beans.left(90)
Beans.forward(X)
Beans.left(90)
Beans.forward(Y)

wn.mainloop()


#----------------------------------------------------
