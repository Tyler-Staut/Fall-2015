#Name: Matthew Newton Bowen
#Date: 10 October 2015
#Title: Assignment 4
#Purpose: Turtle Shapes
def main():
    print("This program draws out concentric shapes of many colors.")
    global side
    side = int(input("How many sides would you like the shape to have? (2 - 5) "))
    while side <= 1:
        side = int(input("The number of sides is invalid, please try again: "))
    global numShapes
    numShapes = int(input("How many shapes would you like to draw? "))
    while numShapes <= 0:
        if numShapes ==0:
            print("The number of shapes must be greater than zero.")
        elif numShapes < 0:
            print("The number of shapes can not be negative.")
        numShapes = int(input("Please input a valid integer for the amount of shapes: "))
    global length
    length = int(input("How long would you like the sides of the shapes to be? "))
    while length <= 0:
        if length ==0:
            print("The side length must be greater than zero.")
        elif length < 0:
            print("The side length can not be negative.")
        length = int(input("Please input a new length of valid size: "))   

def turtleProgram():
    import turtle
    import random
    turtle.title("CPSC 1301 Assignment 4 MBowen")
    turtle.speed(0)
    for x in range(1,(numShapes+1)):
        if 2 <= side <= 5:
            turtle.color(random.random(),random.random(),random.random())
            turtle.begin_fill()
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)
            turtle.left(360/numShapes)
            turtle.end_fill()
        if side == 6:
            turtle.color(random.random(),random.random(),random.random())
            turtle.begin_fill()
            turtle.forward(length)
            turtle.left(360/side)
            turtle.forward(length)
            turtle.left(360/side)
            turtle.forward(length)
            turtle.left(360/side)
            turtle.forward(length)
            turtle.left(360/side)
            turtle.forward(length)
            turtle.left(360/side)
            turtle.left(360/numShapes)
            turtle.end_fill()
        if side == 7:
            turtle.color(random.random(),random.random(),random.random())
            turtle.begin_fill()
            turtle.forward(length)
            turtle.left(360/side)
            turtle.forward(length)
            turtle.left(360/side)
            turtle.forward(length)
            turtle.left(360/side)
            turtle.forward(length)
            turtle.left(360/side)
            turtle.forward(length)
            turtle.left(360/side)
            turtle.forward(length)
            turtle.left(360/side)
            turtle.left(360/numShapes)
            turtle.end_fill()
    turtle.mainloop()
        
main()
turtleProgram()