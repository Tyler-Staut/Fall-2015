#Author: Tyler R. Staut
#File Name: TylerStautLab34.py
#Date: Nov 18, 2015
#Description: Lab34

#-----IMPORTS-----#
import random   #Needed to get randomness
#-----------------#

#----------FUNCTIONS----------#
def openFile(): #definition that Opens file
    listOfNums = [] #List
    numFile = open("numbers.txt")   #Opens file when called
    
    
    for line in numFile:    #for loop
        fields = line.strip(" ")    #Gets rid of the newline characters
        
        listOfNums.append(fields.strip())   #Append the line to the list
    
    numFile.close() #Close file
    return listOfNums   #Return the list
        
def randPicker(list):   #Definition that randomly picks an item from the list
    randIndx = random.randint(0, len(list)-1)   #Randomly chooses an index from the list created earlier
    item = list[randIndx]   #Gets the item
    return item #returns the item

def numToList(stringie):    #Definition that takes the list and splits it up 
    listOfThingies = [] #List
    
    for thingie in stringie:    #For loop to split up list
        listOfThingies.append(thingie)  #Yes I used baby language because I didnt know what else to do
        
    return listOfThingies   #Returns new list

def listModifier(list): #Creates a list of length list it was given and makes it a bunch of --------
    modifiedList = []   #list
    
    for item in list:   #for loop 
        modifiedList.append('-')    #makes the -----
        
    return modifiedList #returns the list

def main(): #Definition for main
    number = numToList(randPicker(openFile()))  #Gets the number list
    secret_number = listModifier(number)    #Makes the ---- list
    
    newList = secret_number #Copies the ---- list
    
    start = 1   #For the while loop
    while start != 0:   #While loop 
        
        if newList == number:   #The final part
            print("The number is {}".format(''.join(number)))
            break
        
        guess = input("{} Guess: ".format(newList)) #The guess
        
        if guess not in (number):   #if not in list say not in list
            print("Not in list")
        
        if guess in newList:    #If already in list say it
            print("Already in list")
        
        
                    
        for digit in range(len(number)):    #For loop to check if guess is in list
            
            if guess == number[digit]:  #If so
                
                newList[digit] = number[digit]  #Replace it
            
#------------------------------#     
  
#-----MAIN-----#      
main()  #Calls main
#--------------#


