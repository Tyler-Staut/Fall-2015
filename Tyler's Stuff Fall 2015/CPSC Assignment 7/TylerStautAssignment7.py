#Author: Tyler R. Staut
#File Name: TylerStautA7.py
#Date: Dec 2, 2015
#Description: Draw a triangle within a larger triangle.

#-----LISTS-----#
listOfCommands = []
#---------------#

#-----IMPORTS-----#
import turtle   #Imports Trutle
import random   #Imports Random
#-----------------#

#-----TURTLE-----#
Beans = turtle.Turtle() #Renames the turtle
Beans.hideturtle()      #Hides the turtle because the triangle turtle thing makes it look weird to me
#----------------#

#----------DEFINITIONS----------#
def makeList(): #Definition that Makes the list of commands
    commands = open("moves.txt")    #Opens the moves file
    for line in commands:   #For loop to itterate through the list
        line.split()    #Splits up the lines
        line = line.strip() #Gets rid of newline character
        listOfCommands.append(line) #Makes a list of the items in the file
    commands.close()    #Closes the file
    
def getCommand(listOfCommands): #Definition that gets the command from the list
    for item in listOfCommands: #For loop to go through the commands
        if item[:4] == 'goto':  #Checks the command
            start = item.index("(") #Used to find location of the int
            mid = item.index(",")
            end = item.index(")")
            
            x = int(item[start+1:mid])  #Gets the x position
            y = int(item[mid+1:end])    #Gets the y position
            
            goto(x, y)  #Calls goto function
            
        elif item[:5] == 'color':   #Checks the command
            colour()    #Calls color function
        
        elif item[:6] == 'jumpto':  #Checks the command
            start = item.index("(")
            mid = item.index(",")
            end = item.index(")")
            
            x = int(item[start+1:mid])  #Gets the x position
            y = int(item[mid+1:end])    #Gets the y position
            
            jumpto(x, y)    #Calls jumpto command
        
        elif item[:6] == 'circle':
            start = item.index('(')
            end = item.index(')')
            
            r = int(item[start+1:end])
            
            circles(r)
            
        elif item[:6] == 'square':
            start = item.index('(')
            end = item.index(')')
            
            sl = int(item[start+1:end])
            
            squares(sl)
            
        else:   #Checks the command for anything other then what is stated aboce
            continue    #Skips command
        
    
def goto(x,y):  #Definition for goto command
    Beans.goto(x,y) #Makes turtle go to the point x,y without lifting the pen
    
def colour():   #Definition for color command
    Beans.color(random.random(), random.random(), random.random())  #Changes the color of the turtle using random number generators to make color

def jumpto(x,y):    #Definition for jumpto command
    Beans.penup()   #Lifts turtle up
    Beans.goto(x, y)    #Moves him
    Beans.pendown() #Puts the turtle back down

def circles(r): #Definition for making circles
    Beans.circle(r) #Makes the turtle go in a circle

def squares(sl):    #Definition for making a square
    Beans.forward(sl)
    Beans.right(90)
    Beans.forward(sl)
    Beans.right(90)
    Beans.forward(sl)
    Beans.right(90)
    Beans.forward(sl)
    Beans.right(90)
    

def main(): #Main Definition
    makeList()  #Call function to make list
    getCommand(listOfCommands)  #Calls function to get the commands and run them
#-------------------------------#

#-----MAIN-----#
main()  #Calls main function
#--------------#

#-----EXTRAS-----#
turtle.mainloop()   #Keeps turtle on the screen
#----------------#

