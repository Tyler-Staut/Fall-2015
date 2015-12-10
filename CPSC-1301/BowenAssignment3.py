#Name: Matthew Newton Bowen
#Date: 27 September 2015
#Title: Assignment 3
#Prupose: Turtle Game
import random
import turtle
game = 'Y'
score = 0
while game == "Y" or game == 'y' :      #Makes it so that an input of 'Y' or 'y' would keep the loop going
    turtle.reset()                      #Resets the turtle position
    turtle.screensize(1000,700)         #Sets up canvas size for turtle
    turtle.setup(1000,700)              #Sets up screen size for turtle
    x1 = random.randint(-450, 250)      #Generates random x value for square to begin at
    y1 = random.randint(-300, 125)      #Generates random y value for square to begin at
    turtle.color("Green")
    turtle.shape("turtle")
    turtle.showturtle()
    turtle.penup()
    turtle.goto(x1, y1)                 #Sends turtle to randomly generated coordinates
    turtle.pendown()
    turtle.forward(200)                 #Begins drawing first square
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.penup()
    turtle.goto((x1+50),(y1+50))        #Sends turtle to location to begin second square
    turtle.pendown()
    turtle.pencolor("Red")
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.penup()
    x=turtle.numinput("Input","Enter x coordinate")     #Gets user input
    y=turtle.numinput("Input","Enter y coordinate")     #Gets user input
    turtle.goto(x,y)                                    #Sends turtle to user inputed coordinates
    if x >= (x1+50) and x <= (x1+150) and y >= (y1+50) and y <= (y1+150):   #If turtle is in smaller square.
        score = score + 2                                                   #2 points for turtle in smaller square
        turtle.write("  You are in!  Score: %d" %score)
    elif x >= x1 and x <= (x1 + 200) and y >= y1 and y <= (y1 + 200):       #If turtle is in larger square.
        score = score + 1                                                   #1 point for turtle in larger square.
        turtle.write("  Almost there!  Score: %d" %score)
    else:                                                #Turtle not in any square
        score = score - 1                                # - 1 point if turtle not in either square.
        turtle.write("  We missed you!  Score: %d" %score)
    game = turtle.textinput("Player Input", "Would you like to continue? (Y/N)") #Asks user to continue
turtle.clear()                                          #Clears all the squares
turtle.write("  Game Over.  Your Score is %d" %score)   #Gives final score
turtle.mainloop()                                       #Keeps turtle on screen
