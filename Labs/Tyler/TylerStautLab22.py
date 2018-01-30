#Author: Tyler R. Staut
#File Name: TylerStautLab22.py
#Date: 10/14/2015
#Description: Simple Dice Game, not to be confused with the Triple A Developers DICE

#-----IMPORTS-----#
import random   #Imports random module
#-----------------#

#----------DEFINITIONS----------#
def Roll_Dice():
    global roll_1   #Makes function global
    global roll_2   #Makes function global
    roll_1 = random.randint(1,6)    #Generates random number between 1 and 6
    roll_2 = random.randint(1,6)    #Generates random number between 1 and 6
    print("First dice landed on: %d\nSecond dice landed on: %d" % (roll_1, roll_2))

def Compare(roll_1, roll_2, bet1, bet2, bet3):
    if bet1 == roll_1 + roll_2:     #Checks the bet to the sum of the Rolls
        return True
    elif bet2 == roll_1 + roll_2:   #Checks the bet to the sum of the Rolls
        return True
    elif bet3 == roll_1 + roll_2:   #Checks the bet to the sum of the Rolls
        return True     #Returns True
    else:
        return False    #Returns False

def Main():     #Main function
    start = 1       #Variable used to determine if the program needs to restart
    while start == 1:
        bet1 = float(input("Place first bet: "))    #First bet
        while bet1 not in range(2, 13):     #Checks if it is valid (Between 2 and 13 because the sum of two dice cannot equal 1 because the lowest value would be 2 and the highest would be 12)
            bet1 = float(input("Bet was invalid, use value between 1-12. Place first bet: "))
        
        bet2 = float(input("Place second bet: "))   #Second bet
        while bet2 not in range(2, 13):     #Checks if it is valid
            bet2 = float(input("Bet was invalid, use value between 1-12. Place second bet: "))
        
        bet3 = float(input("Place third bet: "))    #Third bet
        while bet3 not in range(2, 13):     #Checks if it is valid
            bet3 = float(input("Bet was invalid, use value between 1-12. Place third bet: "))
        
        Roll_Dice()     #Calls function to roll dice
        
        if Compare(roll_1, roll_2, bet1, bet2, bet3) == True:   #Checks if definition is true
            print("One of your bets matched the total!")
            print("YOU WIN!")  #Words of encouragement so that the user plays again and loses the money they got from playing
            start = int(input("Do you want to continue? (1 for yes, 0 for no)"))
            while start not in (1,0):   #Used to restart and try again
                start = int(input("Do you want to continue? (1 for yes, 0 for no)"))
        else:       #Otherwise it prints that you lose
            print("None of your bets add up to be the total.")
            print("YOU LOSE!")  #Words of encouragement so that the user plays again and spends all their money
            start = int(input("Do you want to continue? (1 for yes, 0 for no)"))
            while start not in (1,0):   #Used to restart and try again
                start = int(input("Do you want to continue? (1 for yes, 0 for no)"))

#-------------------------------#

#-----PROGRAM-----#
Main()      #Runs Program
#-----------------#