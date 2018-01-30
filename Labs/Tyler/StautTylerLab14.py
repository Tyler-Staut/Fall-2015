#Author: Tyler R. Staut
#File Name: TylerStautLab14
#Date: 9/23/2015
#Description: Does lots of challenge problems all in one program!

#-----Imports-----
from math import *
#-----------------

def menu():
    print('''What do you want to do? 
    1. Absolute Value
    2. Number Tester
    3. Is it Odd or Even?
    4. Quit Program - (WARNING: QUITS PROGRAM!)''') #Added this last one because it was funny


#----------DEFINITIONS----------
def program1():     #For the first program
    print("\nWelcome to Absolute Value!")
    print("Enter a value and we will give you the Absolute Value.")
    value = int(input("Enter an Integer: "))
    absValue = abs(value)
    print("The absolute value of %d is %d." % (value, absValue))

def program2():     #For the second Program
    print("\nWelcome to Number Tester!")
    print("Enter a value and we will give you information about it.")
    value = int(input("Enter an Integer: "))
    #-----PART 1
    if value > 20:
        print("%d is greater than 20." % value)
    else:
        print("%d is less than or equal to 20." % value)
    #-----PART 2
    if value < 10:
        print("%d is less than 10." % value)
    else:
        print("%d is greater than 10." % value)
    #-----PART 3
    if 10 <= value <= 20:
        print("%d is between 10 and 20." % value)
    else:
        print("%d is not between 10 and 20." % value)
    #-----END


def program3():     #For the third program
    print("\nWelcome to, IS IT EVEN, OR IS IT ODD!!!")
    print("Enter a value and we will tell you if it is Even or Odd.")
    value = int(input("Enter an Integer: "))
    if value % 2 == 0:
        print("Your number is Even.")
    else:
        print("Your number is Odd.")
#-------------------------------

choice = 0  #First option, all others will follow. 1, 2, 3, 4 (to quit)
while choice == 0:
    menu()
    choice = int(input("Enter number of program you want to run: "))
    if choice in (1, 2, 3, 4):
        while choice == 1:
            choice = 0
            program1()
            choice = int(input("1 to replay, 0 to go to menu: "))
            while choice not in (1, 0):
                choice = int(input("Input was wrong. Try Again with input 1 or 0: "))
        while choice == 2:
            choice = 0
            program2()
            choice = int(input("1 to replay, 0 to go to menu: ")) * 2    #Used times 2 so that start can equal 2 if user enters 1
            while choice not in (2, 0):
                choice = int(input("Input was wrong. Try Again with input 1 or 0: "))
        while choice == 3:
            choice = 0
            program3()
            choice = int(input("1 to replay, 0 to go to menu: ")) * 3   #Used time 3 so that start can equal 3 if user enters 1
            while choice not in (3, 0):
                choice = int(input("Input was wrong. Try Again with input 1 or 0: "))
        while choice == 4:  #Quits Program. I tried to add humor to it lol.
            this_does_nothing = input("Are you sure you want to quit, you will lose all of your progress. Yes or No: ")
            print("The program has quit unexpectedly.")
            print("Have a Nice Day!")
            break
    else:
        break
    
        

    