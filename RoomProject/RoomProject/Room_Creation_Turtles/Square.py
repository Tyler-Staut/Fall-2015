'''
Created on Sep 5, 2015

@author: Matt
'''


import turtle

#Can be substituted
length = float(input("What is the length of the square? "))
width = float(input("What is the width of the square? "))
#-------------------

turtle.forward(width)
turtle.left(90)
turtle.forward(length)
turtle.left(90)
turtle.forward(width)
turtle.left(90)
turtle.forward(length)
turtle.mainloop()

