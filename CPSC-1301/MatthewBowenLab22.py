#Name: Matthew Newton Bowen
#File Name: MatthewBowenLab22
#Date: 14 October 2015
#Description: Dice Game
import random
begin = 'yes' #Begins loop
def Roll_Dice():
    global roll #Makes it global
    roll = random.randint(1,6) #Selects random number from 1 to 6
    return roll
def Compare(roll1,roll2,bet1,bet2,bet3): #Defines comparison function
    global bet
    if (roll1+roll2) == bet1: #If bet 1 is equal to the sum, it returns true
        bet = bet1
        return True
    elif (roll1+roll2) == bet2:  #If bet 2 is equal to the sum, it returns true
        bet = bet2
        return True
    elif (roll1+roll2) == bet3:  #If bet 3 is equal to the sum, it returns true
        bet = bet3
        return true
    elif (roll1+roll2) != bet1 or (roll1+roll2) != bet2 or (roll1+roll2) != bet3: #It returns false if not
        return False
def main():
    bet1 = int(input("Please, place your first bet (Between 2 and 12): ")) #Place input
    while bet1 < 2 or bet1 > 12: #Inpur validation
        bet1 = int(input("Please, enter an integer between 2 and 12 for your first bet: "))
    bet2 = int(input("Please, place your second bet (Between 2 and 12): "))
    while bet2 < 2 or bet2 > 12:
        bet2 = int(input("Please, enter an integer between 2 and 12 for your second bet: "))
    bet3 = int(input("Please, place your third bet (Between 2 and 12): "))
    while bet3 < 2 or bet3 > 12:
        bet3 = int(input("Please, enter an integer between 2 and 12 for your third bet: "))
    roll1 = Roll_Dice() #Calls function and assigns value to roll1
    roll2 = Roll_Dice()
    totalroll = roll1 + roll2
    print("\nDice #1 landed on %d" %roll1)
    print("Dice #2 landed on %d" %roll2)
    print("\nThe combined total is %d" %totalroll)
    Compare(roll1, roll2, bet1, bet2, bet3) #Calls comparison function to tell if true
    if Compare(roll1, roll2, bet1, bet2, bet3) == True:
        print("\nYou bet on %d and won! Congratulations!" %bet)
    elif Compare(roll1, roll2, bet1, bet2, bet3) == False:
        print("\nNone of your bets matched the total. You Lose!")
while begin == 'yes': #Keeps loop of game going until user wants to exit
    main()
    begin = input("\nPlay again? (yes or no) ")
print("Thank you for playing!")