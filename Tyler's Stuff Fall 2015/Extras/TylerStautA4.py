# Purpose: This program uses turtle graphics to make shapes
# of all different colors and sizes on the screen.
# Author: Tyler R. Staut
# Date: 10/11/15
import turtle
import random

print("Welcome to the program that draws out squares of many colors in a cool formation.")  #Descriptive Message



Beans = turtle.Turtle()
turtle.title("CPSC1301 Assignment 4 - TStaut")


def square():
    Beans.reset()
    size = int(input("How big do you want the shapes to be? (1-10): "))
    while size not in range(1, 11):
        print("Input was wrong, please try again.")
        size = int(input("How big do you want the shapes to be? (1-10): "))
    
    Beans.hideturtle()
    
    x = 0.5 * (size * 25)   #Caculation to give x coord.
    Beans.goto(-x,0)    #Used to center the image
    for j in range(1, 9):   #Used to make the next part repeat
        Beans.color(random.random(), random.random(), random.random())
        Beans.begin_fill()
        for i in range(5):  #Used to loop next part
            Beans.forward(size * 25)
            Beans.left(90)
        Beans.end_fill()
        Beans.penup()   #So the turtle doesnt draw everywhere
        Beans.left(45)  #So the turtle rotates
        Beans.pendown() #So the turtle does the next task

    
        
def main(): #Main
    start = 1
    while start == 1:
        square()
        start = int(input("Enter 1 to use again, 0 to exit."))
        if start == 0:      #If statement
            print("Hope you enjoyed! Goodbye!") #Closing message
            break
        else:
            continue
    

main()  #Calls Main

Beans.mainloop()   #Keeps turtle on the screen