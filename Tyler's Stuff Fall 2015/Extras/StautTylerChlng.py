#Author: Tyler R. Staut
#File Name: StautTylerChlng
#Date: 9/23/2015
#Description: This is for the Challenge Bonus Points

#-----IMPORTS-----
from random import randint
import time
#-----------------

#----------------------START INFO STUFFS--------------------
print("This is the Random Number Game!!!")
print("Today you will have the most imponderable joy of trying to guess my number.")
#-----------------------------------------------------------

ready = input("Are you ready? Yes or No: ")     #Asks user if they are ready to start
play = 1    #Sets if the loop will repeat at the end of the game
while play == 1:
    play = 0    #Sets to 0 to stop infinite loop
    if ready.lower() in ('yes', 'no'):
        print("Let me think of a number.")  #I thought I would try something nifty
        time.sleep(2)   #It worked
        print("I have a number. Time for you to guess.")    #He really doesnt. He makes it up after just in spite of itself.
        randNum = randint(1, 50)    #Creates random number between 1 and 50
        num = int(input("Your Guess: "))
        while num != randNum:   #Loop to see if number is either greater or less than the number he got.
            if num > randNum:   #If it is above tell user that it is too high of a number
                print("You were a bit too high with that guess. Try Again.")
                num = int(input("Your Guess: "))
            elif num < randNum: #Otherwise it is too small of a number
                print("You were a bit too low with that guess. Try Again.")
                num = int(input("Your Guess: "))
        if num == randNum:  #But if you get it right he will reward you with words such as, it, and you, oh and got.
            print("You got it!")
            print("Would you like to play again?")  #Asks user if they want to play again
            play = int(input("To play again enter 1, otherwise enter 0: ")) #User can chose if they want to stop or not, but why would they. Im sure they could list many reasons why not to but thats besides the point.
            
            
