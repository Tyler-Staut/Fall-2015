#Name: Matthew Newton Bowen
#File Name: MatthewBowenLab32
#Date: 13 November 2015
#Description: GET TEH TABLES!
global ListII
ListII = []         #Initiates lists
MultList = []

def createTable():
    for x in range(1,13):       #Creates 2D list containing the things to be multiplied
        for y in range(1,13):
            MultList.append([x,y])
    return(MultList)

def printTable(ListI):
    
    for z in range(len(ListI)):                             #For spacing
        if len(str(ListI[z][0] * ListI[z][1])) == 1:        #If the length of the digit is 1, add 2 spaces
            print(str((ListI[z][0] * ListI[z][1]))+"  ", end = " ")
        if len(str(ListI[z][0] * ListI[z][1])) == 2:        #If the length of the digit is 2, add 1 space
            print(str((ListI[z][0] * ListI[z][1]))+" ", end = " ")
        if len(str(ListI[z][0] * ListI[z][1])) == 3:        #If the length of the digit is 3, add no spaces
            print(str((ListI[z][0] * ListI[z][1])), end = " ")
        if (z+1) % 12 == 0:                         #If divisible by 12, then make on a new line
            print()
        ListII.append(ListI[z][0] * ListI[z][1])        #builds list of values in the table
    return ListII
        
def findProduct(I1,I2,L1):
    productNum = L1[(I1-1)+(12*(I2-1))]         #multiplies the first integer by the second
    print()
    print(productNum)
    
def main():
    printTable(createTable())       #Prints table
    go = "y"
    while go == 'y':            #loop
        I3 = int(input("Please enter the first value: "))       #Gets inputs
        while I3 > 12 or I3 < 1:
            I3 = int(input("Please input a value between 1 and 12: "))
        I4 = int(input("Please enter the second value: "))
        while I4 > 12 or I4 < 1:
            I4 = int(input("Please input a value between 1 and 12: "))
        findProduct(I3, I4, ListII)             #Prints out value
        go = input("Go again? (y/n): ")

main()