#Name: Matthew Newton Bowen
#Date: 04 December 2015
#Title: Assignment 7
#Purpose: Final Turtle

import turtle           #Imports
import random
LineList = []           #List Initialization

def lineSplit():                    #Splits the lines of text and puts them in the list.
    myFile = open("moves.txt")  #Opens the file    
    for line in myFile:
        line.split()
        line = line.strip()
        LineList.append(line)       #Stores the lines of text into the list
    return LineList
    myFile.close()              #Closes file
    
def Moving(L1):
    for x in range(len(L1)):        #Executes the turtle commands
        if "goto" in L1[x]:             #If goto:
            L1[x] = L1[x].split("(")    #Splits the line by "("
            del L1[x][0]                #Deletes the other end ")"
            L1[x] = L1[x][0][0:-1]      #Stores each value of the list as only the coordinates
            L1[x] = L1[x].split(",")        #Splits the coordinates by the comma between
            for y in range(len(L1[x])):
                L1[x][y] = int(L1[x][y])    #Converts the strings into integers
                turtle.pendown()            #Pen down
                turtle.goto(int(L1[x][0]), int(L1[x][1]))       #Sends the turtle to the x,y coordinates
        if "jumpto" in L1[x]:           #If jumpto:
            L1[x] = L1[x].split("(")    #Splits the line by "("
            del L1[x][0]                #Deletes the other end ")"
            L1[x] = L1[x][0][0:-1]          #Stores each value of the list as only the coordinates
            L1[x] = L1[x].split(",")        #Splits the coordinates by the comma between
            for z in range(len(L1[x])):
                L1[x][z] = int(L1[x][z])    #Converts the strings into integers
                turtle.penup()              #Pen up
                turtle.goto(int(L1[x][0]), int(L1[x][1]))       #Sends the turtle to the x,y coordinates
        if "color" in L1[x]:            #If color
            turtle.color(random.random(),random.random(),random.random())   #Defines random color for turtle
        else:
            continue                #If none of the above criteria is met, do nothing
    turtle.mainloop()       #Keeps turtle on the screen 

Moving(lineSplit())         #Calls both functions