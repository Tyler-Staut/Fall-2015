#Author: Tyler R. Staut
#File Name: TylerStautLab20.py
#Date: 10/7/2015
#Description: Does a lot of mathematical things and it's cool


#----------MATH FUNCTIONS----------
def add(a, b):          #Defines the adding function
    print("Adding %d + %d" % (a, b))
    answer = a + b
    return answer

def subtract(a, b):     #Defines the subtracting function
    print("Subtracting %d - %d" % (a, b))
    answer = a - b
    return answer

def multiply(a, b):     #Defines the Multiplying function
    print("Multiplying %d * %d" % (a, b))
    answer = a * b
    return answer

def divide(a, b):       #Defines the dividing function
    print("Dividing %d and %d" % (a, b))
    answer = a / b
    return answer
#----------------------------------

#----------MAIN----------
def main():     #The main function
    start = 'continue'
    while start == 'continue':
        menu()
        a = int(input("Enter the first number: "))  #Input for variable a
        while a < 0:
            a = int(input("Try again: "))
            
        b = int(input("Enter the first number: "))  #Input for variable b
        while b < 0:
            b = int(input("Try again: "))
        if choice == 1:     #Adding Program  
            value1 = add(a, b)
            print("The answer is %d." % value1)
        elif choice == 2:   #Subtracting Program
            value2 = subtract(a, b)
            print("The answer is %d." % value2)
        elif choice == 3:   #Multiplying Program
            value3 = multiply(a, b)
            print("The answer is %d." % value3)
        elif choice == 4:   #Dividing Program
            value4 = divide(a, b)
            print("The answer is %d." % value4)
        
        start = input("Do you want to continue or exit? (continue/exit): ")     #Continue or exit loop thingy
        while start.lower() not in ('continue', 'exit'):
            start = input("Do you want to continue or exit? (continue/exit): ") #Otherwise if not the things do the thing again
            
#------------------------        
 
#----------MENU----------           
def menu():     #Creates the menu System
    print("1.    Add")
    print("2.    Subtract")
    print("3.    Multiply")
    print("4.    Divide")
    global choice   #Makes the choice available for everyone
    choice = int(input("What program do you want to run? (1-4): "))
    while choice not in (1, 2, 3, 4):
        choice = int(input("Try again. (1-4): "))   #else if choice is wrong try again
#------------------------   
    
    

#------RUN THE PROGRAM------
main()  #Start of program
#---------------------------