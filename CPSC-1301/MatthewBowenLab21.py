#Name: Matthew Newton Bowen
#File Name: MatthewBowenLab21
#Date: 12 October 2015
#Description: Magic 9 ball
import random
def magic(a): #Defines the magic function, giving a response for each.
    if a == 1:
        print("\nIt is certain.")
    elif a == 2:
        print("\nAffirmative.")
    elif a == 3:
        print("\nWithout a doubt.")
    elif a == 4:
        print("\nResponse unknown. Please try again.")
    elif a == 5:
        print("\nThe voices have gone silent, ask again later.")
    elif a == 6:
        print("\nIt is best you do not know now, try again at a later time.")
    elif a == 7:
        print("\nNo, why would you EVER even THINK about asking that? What is wrong with you?")
    elif a == 8:
        print("\nThis is not to be. No.")
    elif a == 9:
        print("\nAll is not at peace in the world, the spirits say no.")
def main(): #Defines the main function
    start = "yes" #Starts the loop
    global a
    while start != "end": #Loop
        input("Please enter a yes or no question, and a response will be supplied. ")
        a = random.randint(1,9) #Random number between 1 and 9
        magic(a) #Calls magic function
        start = input("\nPlease enter 'end' to end the program, or anything else to go again. ")
main() #Calls main function
print("Thank you for using the Magic 9 Ball! Have a wonderful day!") #Thank You!!!!
    
        