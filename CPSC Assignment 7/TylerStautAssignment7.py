#Author: Tyler R. Staut
#File Name: TylerStautAssignment7.py
#Date: Dec 2, 2015
#Description: Draw a triangle within a larger triangle.

#-----LISTS-----#
listOfCommands = []
#---------------#

#-----IMPORTS-----#
import turtle
import random
#-----------------#

#-----TURTLE-----#
Beans = turtle.Turtle()
Beans.hideturtle()
#----------------#

#----------DEFINITIONS----------#
def makeList():
    commands = open("moves.txt")    #Opens the moves file
    for line in commands:   #For loop to itterate through the list
        line.split()    #Splits up the lines
        line = line.strip() #Gets rid of newline character
        listOfCommands.append(line) #Makes a list of the items in the file
    commands.close()    #Closes the file
    
def getCommand(listOfCommands):
    for item in listOfCommands:
        if item[:4] == 'goto':
            start = item.index("(")
            mid = item.index(",")
            end = item.index(")")
            
            x = int(item[start+1:mid])
            y = int(item[mid+1:end])
            
            goto(x, y)
            
        elif item[:5] == 'color':
            colour()
        
        elif item[:6] == 'jumpto':
            start = item.index("(")
            mid = item.index(",")
            end = item.index(")")
            
            x = int(item[start+1:mid])
            y = int(item[mid+1:end])
            
            jumpto(x, y)
            
        else:
            continue
        
    
def goto(x,y):
    Beans.goto(x,y)

def colour():
    Beans.color(random.random(), random.random(), random.random())

def jumpto(x,y):
    Beans.penup()
    Beans.goto(x, y)
    Beans.pendown()

def main():
    makeList()
    getCommand(listOfCommands)
#-------------------------------#

#-----MAIN-----#
main()  #Calls main function
#--------------#

#-----EXTRAS-----#
turtle.mainloop()
#----------------#

