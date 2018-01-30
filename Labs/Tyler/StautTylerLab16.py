#Author: Tyler R. Staut
#File Name: StautTylerLab16.py
#Date: 9/28/2015
#Description: Number Counter

#----------FIRST PART OF SHOWING THE NUMBERS GOING UP AND DOWN AND EVEN AND ODD----------

#-----FIRST SET-----
print("Numbers from 1 to 100")

for i in range(1, 101, 1):  #Prints numbers from 1 to 100 with step 1
    print(i, end=" ")
print("\n")
#-------------------

#-----SECOND SET-----
print("\n")
print("\nNumbers from 100 to 1")

for i in range(100, 0, -1): #Prints numbers from 100 to 1 with a negitive step of 1
    print(i, end=" ")
print("\n")
#--------------------

#-----THIRD SET-----
print("\n")
print("All even numbers between 1 and 100")

for i in range(2, 101, 2):  #prints even numbers between 1 and 100
    print(i, end=" ")
print("\n")
#-------------------

#-----FOURTH SET-----
print("\n")
print("All odd numbers between 1 and 100")

for i in range(1, 100, 2):  #Prints odd numbers between 1 and 100
    print(i, end=" ")
print("\n")
#--------------------
#----------------------------------------------------------------------------------------

#----------USER INPUT----------
print("\n")
print("Now time for you to put in your own number for the program use.")    #Tells user what is about to happen next

number = int(input("Enter an integer: "))   #Asks user for their number to input

#-----CHALLENGE-----
while number <= 0:  #Makes the user input an integer that is positive including 0 because technically it is in math for all intensive purposes
    number = int(input("Integer cannot be negative. Try Again: "))
#-------------------

#-----PART 1-----            #This is a repeat from the first part just using the user input instead so comments will be light for these next parts
print("\n")
print("Numbers from 1 to %d" % number)  #I used the thing that replaces %d with the number

print("\n")
for i in range(1, number + 1):
    print(i, end=' ')

#-----PART 2-----
print("\n")
print("Numbers from %d to 1" % number)

print("\n")
for i in range(number, 0, -1):
    print(i, end=' ')

#-----PART 3-----
print("\n")
print("Even Numbers from 1 to %d" % number)

print("\n")
for i in range(2, number + 1, 2):
    print(i, end=' ')
    
#-----PART 4-----
print("\n")
print("Odd Numbers from 1 to %d" % number)

print("\n")
for i in range(1, number + 1, 2):
    print(i, end=' ')
#------------------------------
#This is the end of the program
