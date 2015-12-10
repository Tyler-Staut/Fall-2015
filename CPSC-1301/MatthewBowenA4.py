#Name: Matthew Newton Bowen
#Date: 10 October 2015
#Title: Assignment 4
#Purpose: Turtle Shapes
def main():
    print("This program draws out concentric hexagons of many colors.")
    global numHex
    numHex = int(input("How many hexagons would you like to draw? (A value between 25 and 360) "))
    while numHex < 25 or numHex > 360: #Input validation so the number of hexagons is no less than 25, and no larger than 360
        if numHex < 25:
            print("The number of hexagons must be greater than or equal to 25.\n")
        elif numHex > 360:
            print("The number of hexagons can not be greater than 360.\n")
        numHex = int(input("Please input a valid integer for the amount of hexagons: "))
    global length
    length = int(input("How long would you like the sides of the hexagons to be? (A value between 75 and 150) "))
    global length1
    length1 = length
    while length < 75 or length > 150: #Input validation for length of sides
        if length < 75:
            print("The side length must be greater than 75.\n")
        elif length > 150:
            print("The side length can not be greater than 150.\n")
        length = int(input("Please input a new length of valid size: "))   

def turtleProgram():
    import turtle
    import random
    global length
    turtle.title("CPSC 1301 Assignment 4 MBowen") #Makes the title of the graphic box
    turtle.speed(0) #Makes the turtle go rather fast
    for x in range(1,(numHex+1)): #For loop for creating the hexagons, and filling them up
        turtle.color(random.random(),random.random(),random.random()) #Defines a random color
        turtle.begin_fill()
        turtle.forward(length)
        turtle.left(60)
        turtle.forward(length)
        turtle.left(60)
        turtle.forward(length)
        turtle.left(60)
        turtle.forward(length)
        turtle.left(60)
        turtle.forward(length)
        turtle.left(60)
        turtle.forward(length)
        turtle.left(60)
        turtle.end_fill()
        turtle.left(2160/(numHex))
        length = length - (length/numHex) #Shrinks the hexagons by a small ratio in order to create a more impressive shape
    turtle.penup()   
    turtle.goto(5*length1/2, 0) #Sends turtle to a blank spot
    turtle.color("Black")
    turtle.hideturtle()
    turtle.write("You have drawn %d hexagons in this pattern." %numHex) #Captions the turtle graphic
    turtle.mainloop()
        
main() #Calls main function
turtleProgram() #Calls turtle program