#Name - Matthew Newton Bowen
#Date - 09 December 2015
#File - MatthewBowenFINAL   
#Description - Final Hang Man

import random

def createWordList():
    words = []                      #Initializes the list of words from the file
    wordFile = open("wordList.txt") #Opens the file
    for line in wordFile:           
        line =line.strip()          #Strips the words
        words.append(line)          #adds the lines to the list
    wordFile.close()                #Closes the file
    return words                    #Returns list of words from the file

def randomWord(L):
    randword = random.randint(0,(len(L)-1))     #Chooses a random number between 0 and 1 less than the length of the list
    return L[randword]                          #Returns the word stored at the random index

def wordToList(S):
    wordLetters = []                    #Initializes the list of letters in the word
    for element in range(len(S)):       
        wordLetters.append(S[element])  #Appends the list with each letter from the word
    return wordLetters                  #Returns the list of characters that compose the word

def stars(L1):
    astList = []                #Initializes the list of asterisks
    for x in range(len(L1)):
        astList.append("*")     #Adds the same number of asterisks as letters in the word to the list
    return astList              #Returns that list of asterisks

def welcome():
    print("Welcome to the hangman game!\n")             #All your welcome instructions
    print("Instructions:\n")
    print("Try to determine the word by guessing letters.")
    print("If a correct letter is guessed, the respective star will be replaced with that letter.")
    print("If the letter is not in the word, a message will be displayed indicating such.")

def main():
    welcome()                               #Prints out your welcome :)
    go = "yes"                              #Starts out the first loop (To begin the game)
    while go == "yes" or go == "Yes":
        print()                             #Blank Space
        lettersGuessed = []                 #Initialize the list for letters guessed
        Words = createWordList()                        #Gets list of words from file
        randomNumber = randomWord(Words)                #Chooses a random word from that list
        deconstructedWord = wordToList(randomNumber)    #Breaks that word into its characters
        starList = stars(wordToList(randomNumber))      #Makes a list of asterisks of the same length
        copyOfWord = wordToList(randomNumber)           #Copies the deconstructed word for comparison
        actualWord = ""                     #Initializes the actual word
        numIncorrect = 0                    #Initializes the number of incorrect guesses
        for y in range(len(starList)):
            actualWord = actualWord + copyOfWord[y]     #Builds the actual word from the list
        begin = 0                           #Initializes the guessing loop
        while begin == 0:
            for star in range(len(starList)):
                print(starList[star], end = "")         #Prints out the list of asterisks (and letters already guessed)
            print("    ", end = "")                     #Spacing
            print("Please, enter a letter: ", end = "") #User input
            guess = input("")
            if guess in lettersGuessed:
                print("Already guessed.")               #If letter already guessed, prints out this
            if guess not in lettersGuessed:
                lettersGuessed.append(guess)            #If letter not previously guessed, adds to list
            if guess in starList:                       
                print("Already there.\n")               #Prints if letter has been correctly guessed already
            for z in range(len(starList)):
                if guess == deconstructedWord[z]:       #If the guess is in the word
                    starList[z] = deconstructedWord[z]  #Reassign the asterisk in that list with the correct letter
                    deconstructedWord[z] = "*"          #Adds the asterisk back to the word being compared
                if starList == copyOfWord:              #If all letters have been correctly guessed.
                    begin = 1                           #ends the guessing loop
            if guess not in copyOfWord:                 #If the guess isn't in the word
                print("Not in the word.\n")             #It prints out a respective statement
                numIncorrect += 1       #Increases the amount of incorrect guesses by 1
        print()                                         #Blank Space
        print("The word was: {0}".format(actualWord))   #Prints out the actual word, confirming the win
        print()                                         #Blank space
        print("You guessed incorrectly {0} times.".format(numIncorrect))    #Prints out the number of incorrect guesses
        go = input("Would you like to play again? (yes/no): ")  #Would you like to play again?
    print("Thank you for playing!")     #If not, prints out a thanks! <3
    
main()                  #Calls everything
        
        #Thanks for a great semester, and have a wonderful holiday!!!!  
    