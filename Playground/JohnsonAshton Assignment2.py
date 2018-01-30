#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Program Name: JohnsonAshton Assignment2.py
#Purpose: This program calculates the amount and price of paint needed to cover
#         any hexagonal area.
#Author: Ashton Johnson
#Date Due: 9/13/15
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#(Given Information:)
#   The cost of paint per gallon is $10.
#   Amount of paint needed per square foot is 0.1 gallon.

#Inform User of Cost
print("The cost of paint per gallon is $10.")
print("The amount of paint needed per square foot is 0.1 of a gallon.\n") #Added newline so to seperate this from input
side = eval(input("In feet, what is the length of each side of the hexagon? "))

#Calculate Given Sides
from math import *  #The * imports everything and allows you to exclude the math. part
area = ((3*sqrt(3))/2)*(side**2)
print("\nThe area of your hexagon is",area,"square feet.")

#Determine Amount of Paint Needed
paintGal = (area*0.1)
print("The amount of paint needed is",paintGal,"gal.")

#Determine the Cost
cost = round((paintGal/10), 2)
print("The cost of",paintGal,"gal. is $",cost)
