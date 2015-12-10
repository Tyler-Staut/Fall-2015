#Author: Tyler R. Staut
#File Name: StautTylerIP1.py
#Date: 9/25/2015
#Description: Independent Programming project #1

#----------WELCOME MESSAGE----------
print("Welcome to the Baggage Fee Calculator!")     #This is just the thing to say welcome to the program, It doesnt really need to be repeated.
print("This airline company charges $25 for the first bag, $35 for the second, and $50 for the rest.\n")
#-----------------------------------


run = 'yes'
while run == 'yes':
    
    #------NAME------
    name = input("What is your name traveler? Name: ")      #Im hoping the name would not change if the user wants to go again
    #---------------                                        #I suppose if a tsa person is using it they would put other peoples name here so i guess it works
    
    #-----INPUTS-----
    bags = int(input("How many bags will you be bringing on your journey? Number of Bags: "))
    #----------------
    
    #----------CACULATIONS----------    #This does calculations so I dont have to later on
    if bags == 0:
        cost_for_bags = 0
    elif bags == 1:
        cost_for_bags = 25
    elif bags == 2:
        cost_for_bags = 25 + 35
    elif bags >= 3:
        cost_for_bags = 25 + 35 + 50 * (bags - 2)
    #-------------------------------
    
    #----------OUTPUTS----------    #A list of possible outputs. If input is negitive the entire place shuts down like American Airlines did lol
    if bags == 0:
        print("There is no charge for %d bags." % bags)
        print("Bon Voyage %s\n" % name)
    elif bags == 1:
        print("You will have to pay $%d for %d bags." % (cost_for_bags, bags))
        print("Bon Voyage %s\n" % name)
    elif bags == 2:
        print("You will have to pay $%d for %d bags." % (cost_for_bags, bags))
        print("Bon Voyage %s\n" % name)
    elif bags >= 3:
        print("You will have to pay $%d for %d bags." % (cost_for_bags, bags))
        print("Bon Voyage %s\n" % name)
    #---------------------------
    
    #-----LOOP CONTINUE OR DISCONTINUE-----    #Would you like to loop? That question will be answered whenever the user gets to this point!!!!!
    run = input("Would you like to run this program again? (Yes/No): ")     #Added to ask user if they wanted to go again.
    while run.lower() not in ('yes', 'no'):
        run = input("Input was incorrect, try again. (Yes/No)")     #Added so only the correct answer will be taken.
    if run.lower() == 'no':
        print("Thank you for using the Baggage Fee Calculator!")    #The End. 
        #I really want to add have a nice day my friend but in French because of the Bon Voyage thing but French has seemed to
        #Have escaped from my memory, oh well. At least it works. So many comments.