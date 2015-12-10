#Name: Matthew Newton Bowen
#File Name: MatthewBowenLab34
#Date: 18 November 2015
#Description: NUMBERSSS

import random

def File():
    numsfromfile = []
    filenums = open("numbers.txt")      #Opens file
    for line in filenums:
        newLine = line.strip()          #Builds list from numbers
        numsfromfile.append(newLine)
    filenums.close()                    #Closes file
    return numsfromfile

def randItem(L):
    randnum = random.randint(0, len(L)-1)   #Gets random index
    return L[randnum]                   #Evaluates that index into the list

def Stripping(S):
    strList = []
    for elem in range(len(S)):          #Builds list from characters in a string
        strList.append(S[elem])
    return strList
    
def Hyphens(L):
    hyphenList = []
    for T in range(len(L)):             #Takes length of inputed list, and makes list of hyphens with that length
        hyphenList.append("-")
    return hyphenList

def main():
    v = 0                   #Initiates loop
    str1 = ""               #Initiates string
    realnum = randItem(File())              #Calls functions
    digitList = Stripping(realnum)
    Hyplist = Hyphens(digitList)
    digitList1 = Stripping(realnum)
    while v == 0:
        for z in range(len(Hyplist)):       #Prints hyphen list
            print(Hyplist[z], end = " ")
        guess = input("Guess: ")            #Takes input
        if guess in Hyplist:                #If it's been guessed before, prints already there
            print("Already there.")
        for w in range(len(Hyplist)):
            if guess == digitList[w]:       #If guess is in the list, replaces hyphens with that number when it occurs
                Hyplist[w] = digitList[w]
                digitList[w] = "-"          #Replaces the number with a hyphen in the other list
            if Hyplist == digitList1:       #Exit the loop when all numbers have been guessed
                v = 1
        if guess not in digitList1:         #If number not in list, prints out
            print("Not in list.")
    print("The number is: ", end = " ")     #Prints final number
    for z in range(len(Hyplist)):           #Builds that number
        str1 = str1 + Hyplist[z]
    print(str1)
                 
main()