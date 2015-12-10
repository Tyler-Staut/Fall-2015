#Author: Tyler R. Staut
#File Name: StautAssignment3.py
#Date: 9/27/2015
#Description: Turtle in a Box game. Try and get a turtle into a box to get points.

#-----IMPORTS-----
from random import randint
import turtle
#-----------------

#----------DEFINITIONS----------
squareSize = 200    #Initial Square size

def square():       #Bigger outside square
    Beans.color("red")
    Beans.penup()
    Beans.goto(pos1, pos2)
    Beans.pendown()
    Beans.forward(squareSize)
    Beans.left(90)
    Beans.forward(squareSize)
    Beans.left(90)
    Beans.forward(squareSize)
    Beans.left(90)
    Beans.forward(squareSize)
    Beans.left(90)
    
def squareTwo():        #Inside Square
    Beans.color("green")
    Beans.penup()
    Beans.goto((pos1 + 50), (pos2 + 50))
    Beans.pendown()
    Beans.forward(squareSize/2)
    Beans.left(90)
    Beans.forward(squareSize/2)
    Beans.left(90)
    Beans.forward(squareSize/2)
    Beans.left(90)
    Beans.forward(squareSize/2)
    Beans.left(90)


def startProgram():     #Tells the program what to do. I could probably work this into the loop but this is the way I know how to do it.
    turtle.setworldcoordinates(-410, -410, 410, 450)    #Sets the size of the canvas so that the square will fit within the screen
    square()
    squareTwo()
    Beans.penup()
    Beans.goto(0, 0)
    

    
def SCORE(points):      #This defines the score turtle thing that shows the score on the top of the screen. 
    Score.reset()
    Score.speed(0)
    Score.hideturtle()
    Score.penup()
    Score.goto(-410, 410)
    Score.pendown()
    Score.forward(820)
    Score.penup()
    Score.goto(-410, 410)
    Score.write("Your Score is: %d" % points, font=("Arial", 12, "bold"))
#---------------------------------

#----------START----------
Beans = turtle.Turtle()     #Names the main turtle Beans
Score = turtle.Turtle()     #Names second turtle Score
points = 0

start = 1

while start == 1:       #Loop
    start = 0
    
    #USED TO GET SECONDARY POSITION
    pos1 = randint(-400, 200)       #Used -400 becaue the turtle starts from the lower left part of the square so the lower left points of the window need to be open for the turtle to use.
    pos2 = randint(-400, 200)
    
    startProgram()  #Starts the program
    
    x1 = turtle.numinput("Input", "Input your X coordinate: ")
    y1 = turtle.numinput("Input", "Input your Y coordinate: ")
    
    Beans.goto(x1, y1)  #Goes to input location
    
    if (pos1 + 50) <= (x1) <= (pos1 + 150) and (pos2 + 50) <= (y1) <= (pos2 + 150):     #Turtle is in the small square
        Beans.write("You are in!")
        points += 2     #Add 2 points
        SCORE(points)
        
    elif (pos1 <= (x1) <= (pos1 + 200)) and (pos2 <= (y1) <= (pos2 + 200)):       #Used to see if the turtle is within the square
        Beans.write("Almost there!")
        points += 1     #Add a point
        SCORE(points)
        
    else:       #Turtle did not make it into or onto a square
        Beans.write("We missed you!")
        points -= 1     #Subtract a point
        SCORE(points)
    
    ans = turtle.textinput("Input", "Do you want to play again? Yes or No: ")   #Loop statement so user can play again
    if ans.lower() in ("yes"):
        Beans.reset()   #Clears the turtle drawings so it can go again on a clean slate
        
        start = 1   #Completes the loop
    else:       #Else clears everything but the score and says game over and leaves score in upper left hand corner
        Beans.reset()
        Beans.color("black")
        Beans.write("Game Over!", move=False, align="center", font=("Arial", 54, "normal"))     #This is to center the Text and make it large enough to properly read that the game is over on screen
        break
    
#-------------------------

turtle.mainloop()   #Keeps window on screen
    
