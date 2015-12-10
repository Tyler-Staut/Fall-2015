#Author: Tyler R. Staut
#File Name: TylerStautFinal.py
#Date: Dec 9, 2015
#Description: This is the end of the Beginning, the final.

#-----IMPORTS-----#
import random
#-----------------#

#----------DEFINITIONS----------#
def createWordList():   #Creates a list from the words
    listOfWords = [] #List
    wordFile = open("wordList.txt") #Opens the file
    
    for line in wordFile:   #for loop     
        fields = line.strip(" ")    #Strips the words
        
        listOfWords.append(fields.strip())  #No more newline characters, they cant act at all.
        
    wordFile.close()    #Closes the file
    
    return listOfWords  #Returns the list

def randomWord(List):   #Definition that will pick a random word
    randWord = random.randint(0, len(List)-1)   #Picks a random number
    item = List[randWord]   #Uses that number to pick from the list
    
    return item #Returns that item from the list

def wordToList(wordString): #Definition to convert a word to a list of its characters
    listOfThingies = [] #List
    
    for char in wordString: #For loop
        listOfThingies.append(char) #Appends the characters of the word
        
    
    return listOfThingies   #Returns the list of the things of the word, characters or whatever

def stars(LOC): #Definition for Literature of Composititon errr I mean list of characters, not English final.
    modedList = []  #List
    
    for item in LOC:    #For loop
        modedList.append("*")   #Astericks WOO!!!
        
    return modedList    #Returns the modified list, GTA V does not like mods onlie so this is bad for that case

def welcome():  #Ello my good sir! Cup of tea, Shine the shoes.
    print("Behold, Hangman the Game!!") #Lots of words
    print("Instructions: ") #Instructions
    print("- Try and figure out the word by guessing one letter at a time.")    #Its GREEN!
    print("- If you guess a letter correctly, the '*' will be replaced with the letter.")   #To me at least, to you it's whatever color
    print("- If the letter is not in the word, it will not be displayed. Sorry.")   #You wanted it to be, it's green for me.
    print("Now lets get started!")
    
def main(): #The main is a lime green though
    word = wordToList(randomWord(createWordList())) #This kicks things off with getting the word
    secret_word = stars(word)   #Then this makes it secret, so dont tell anyone alright
        
    newList = secret_word   #Copy and Pastint lol, no just copies the list
    
    incorrect = 0   #For the BONUS ROUND!!!
    
    start = 1   #Initialization of variable to start
    while start != 0:   #While loop
        if newList == word: #If the word is guessed then you've won
            print("\n")
            print("Congrats! You've Won!!! The word is - {}".format(''.join(word)))
            print("\n")
            print("Wow! You have guessed incorrectly {} number of times!".format(incorrect))
            print("\n")
            play = int(input("Do you want to play again? (1 - yes / 0 - no): "))    #For repeats
            return play #Return answer
        
        guess = input("{} Guess: ".format(newList)) #Guessing time
        
        if guess not in (word): #If not in word say so
            print("Letter is Not in word.")
            incorrect += 1  #This is also for bonus
        
        if guess in newList:    #Otherwise say WOW you already guessed that, you could have guessed something else, there is a list of what you input right on the screen
            print("Letter is Already there.")
            
        
        for char in range(len(word)):   #For loop
            
            if guess == word[char]: #Used to update the new list
                newList[char] = word[char]
                
def playAgain():    #Definition to play again
    welcome()   #Prints welcome
    print("\n")
    play = 1    #Initialization
    while play != 0:
        play = main()   #Runs the main and waits for a response
#------------------------------#

#-----MAIN-----#
playAgain() #Starts program. 
#--------------#
#I made it all the way to line 100, sweet. If you got this far thanks for reading. This class has be very fun. Allons-y!