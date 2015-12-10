#Author: Tyler R. Staut
#File Name: TylerStautLab32.py
#Date: Nov 13, 2015
#Description: Lab 32

#-----LISTS-----#
twoDList = []   #This is a list
#---------------#

#----------FUNCTIONS----------#
def creatTable():   #Definition to create the table
    for across in range(1, 13): #This is for the list length across
        for down in range(1, 13):   #this is for the list length down
            twoDList.append([across, down, across * down])  #This appends the info needed for the list
    
def printTable(twoDList):   #Definition to print table
    count = 0   #Sets up count
    for num in range(len(twoDList)):    #Loop
        count += 1  #Adds one to count
        
        print("%-4s" % (twoDList[num][2]), end='') #I HATE % BUT IT WAS THE ONLY THING I COULD DO, IM SO UPSET
        
        if count % 12 == 0: #Count thingie to make new line
            print() #Empty print for new line

def findProduct(value1, value2, twoDList):  #Definition to find a certain value on a chart of values
    for listThing in twoDList:  #Loop
        if listThing[0] == value1 and listThing[1] == value2:   #Checks both values
            print("\nThe product of {} and {} is {}".format(value1, value2, listThing[2]))  #Prints answer
            
def main(): #Main def
    creatTable()    #Makes table
    printTable(twoDList)    #Prints table
    start = 1   #Initiation of start
    while start != 0:   #loop
        value1 = int(input("Enter first value: "))  #Gets value 1
        while value1 not in range(1, 13):
            value1 = int(input("Enter first value: "))
        
        value2 = int(input("Enter first value: "))  #Gets value 2
        while value2 not in range(1, 13):
            value2 = int(input("Enter first value: "))
        
        findProduct(value1, value2, twoDList)   #Does the thing
        
        start = int(input("1 to continue, 0 to leave")) #Continue? Yes? no?
        while start not in (0,1):
            start = int(input("1 to continue, 0 to leave"))

#-----------------------------#  

#-----MAIN-----#
main()      #calls main
#--------------#