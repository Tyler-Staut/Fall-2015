#Author: Tyler R. Staut
#File Name: TylerStautLab26.py
#Date: Oct 26, 2015
#Description: Does something with names


#-----LIST-----#
namesList = []
#--------------#


#----------DEFINITIONS----------#
def PrintMenu():    #This is the menu thingy, it has a bunch of options
    print("1) List all names")
    print("2) Add name")
    print("3) Number of names")
    print("4) Remove name")
    print("5) Quit")
    
    menuOpt = int(input("Enter an Option: "))   #You can choose option here
    while menuOpt not in range(1,6):
        menuOpt = int(input("Enter an Option: "))   #This verifys option is good, then the option handshapes the code
    if menuOpt == 1:    #Heres an option
        return 1
    elif menuOpt == 2:  #Theres an option
        return 2
    elif menuOpt == 3:  #There is a few more option so yeah
        return 3
    elif menuOpt == 4:  #These are options
        return 4
    elif menuOpt == 5:  #Its great to be a option
        return 5
     
def OpenFileToList():   #Opens file and puts it in a list
    namesFile = open("names.txt")   #Opens file
    
    for line in (namesFile):
        names = line.split(" ")     #Seperates the lines
        namesList.append(names[0].strip())  #Gets rid of new line
        
        
    namesFile.close()   #Closes file
    return namesList    #Returns list, its here that i am really tired of adding boring coments
    
def ListAll(l1):    #Another boring comment to explain that this will list all names in list
    print("The names in the list are:")
    for line in range(len(l1)): #For each line
        print(l1[line]) #It will print that line, WOAH!?!?!?!?!
        
def AddName(l2, name_thing):    #This definition should in theory allow the user to enter a name if I did things right
    if name_thing in namesList: #Checks if name is in list
        print("The name {0} was already in the list.".format(name_thing))   
    elif name_thing not in namesList:   #If not it adds it
        namesList.append(name_thing)
        print("The name {0} was added to the list.".format(name_thing))
        
    return (l2) #Then it returns the list
        
def NumberOfNames(listParamater):       #THis tells the user the number of names
    lT = len(listParamater)
    return lT   #It returns the number
    
def RemoveName(namesList, antiAdd):     #Its like adding a name but inversely
    if antiAdd in namesList:
        namesList.remove(antiAdd)
    else:
        print("Name is not in list.")
    
    return namesList        #It returns list without the name you did not want to have in the list

def main():     #The main function of the program
    menuOpt = PrintMenu()
    while menuOpt != 5:
        
        if menuOpt == 1:        #LIST ALL NAMES
            ListAll(namesList)
            
            
        elif menuOpt == 2:      #ADD NAMES
            add = input("Enter a name you would like to add: ")
            print(AddName(namesList, add))
            
        elif menuOpt == 3:      #NUMBER OF NAMES
            print(NumberOfNames(namesList))
            
        elif menuOpt == 4:      #REMOVE NAMES
            antiAdd = input("Enter a name you would like to remove: ")
            print(RemoveName(namesList, antiAdd))
        menuOpt = PrintMenu()
#-------------------------------#

#-----START-----#
OpenFileToList()    #Puts file into list
main()  #Starts the program
#---------------#