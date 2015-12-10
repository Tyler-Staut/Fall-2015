#Name: Matthew Newton Bowen
#File Name: MatthewBowenLab26
#Date: 26 October 2015
#Description: File I/O

def PrintMenu():                #Defines menu
    print("1) List all names")
    print("2) Add name")
    print("3) Number of names")
    print("4) Remove name")
    print("5) Quit")
    option = int(input("Please enter the number of the option you wish to use: "))
    while option > 5 or option < 1:    #Validates input
        option = int(input("Please enter a valid number of the option you wish to use: ")) #returns the value of each option
    if option == 1:
        return 1
    elif option == 2:
        return 2
    elif option == 3:
        return 3
    elif option == 4:
        return 4
    elif option == 5:
        return 5

def OpenFileToList():       #defines the opening of the file to list
    list1 = [] #initiates list
    fileNames = open("C://names.txt") #Opens the file
    for line in fileNames:
        names = line.split(" ")  #Splits the file
        list1.append(names[0].strip())   #Strips the file
    fileNames.close()
    return list1 #returns the list

def ListAll(L1): #takes each value of the list and prints it out
    for x in range(len(L1)):
        print(L1[x])

def AddName(L2, firstName): 
    if firstName in L2: #Checks to see if the name is already in the list
        print("This name is already in the list.")
    else:
        L2.append(firstName)
    return L2

def NumberOfNames(L3): #gets the amount of names on the list
    return len(L3)

def RemoveName(L4, firstName):
    if firstName in L4:     #Checks to see if the name is in the list, and removes it if it is.
        L4.remove(firstName)
    else:
        print("This name is not in the list.")
    return L4

def Main():                         #Sets up the loop for all the functions, and calls them
    OpenFileToList()
    List = OpenFileToList()
    printOption = PrintMenu()
    while printOption != 5:
        if printOption == 1:
            print(" ")                  #Just adds new lines
            ListAll(List)
            print(" ")
        elif printOption == 2:
            print(" ")
            newName = input("What name would you like to add to the list? ")    #Gets the new name to add
            print(AddName(List, newName))
            print(" ")
        elif printOption == 3:
            print(" ")
            print(NumberOfNames(List))
            print(" ")
        elif printOption == 4:
            print(" ")
            removeName = input("What name would you like to remove from the list? ") #Gets the name to remove
            print(RemoveName(List, removeName))
            print(" ")
        
        printOption = PrintMenu()
    print("Thank you!")
Main()
   