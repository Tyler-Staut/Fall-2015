#Author: Tyler R. Staut
#File Name: TylerStautLab29.py
#Date: Nov 6, 2015
#Description: 1-800 CHALLENGE!!!! JOHN CENA USA OPEN CHALLENGE!!!

list2D = [[1,2,3],[4,5,6],[7,8,9]]  #This is th 2D list

for t in range(len(list2D)):    #This does the things to do printing list
    for y in range(len(list2D)):    #This does the more things because it needs to get items from within lists
        print(list2D[t][y], end=' ')    #This prints it
    print("")   #This makes it go to a new line to do it right

def main(): #Main function to do the things
    row = int(input("Enter a row from above: "))    #Gets row
    while row not in (1,2,3):
        row = int(input("Enter a row from above: "))
    
    column = int(input("Enter a column from above: "))  #Gets column
    while column not in (1,2,3):
        column = int(input("Enter a column from above: "))
    
    print(list2D[row-1][column-1])  #Prints the number at the row and column
    
    
    num = int(input("Enter a number to search for in the list to get the row and column: "))    #Gets user number
    if num in range(1,10):  #Checkes to make sure number is in list
        print("{} is in the 2D list".format(num))   #Prints it is in list
        if num in (1,2,3):  #If it is here it will print out want needs to be printed
            print("{} is in row 1 column {}.".format(num, list2D[0].index(num)+1))
        
        if num in (4,5,6):  #If it is here it will print out want needs to be printed
            print("{} is in row 2 column {}.".format(num, list2D[1].index(num)+1))
            
        if num in (7,8,9):  #If it is here it will print out want needs to be printed
            print("{} is in row 3 column {}.".format(num, list2D[2].index(num)+1))
        
    else:
        print("Number is not in list.") #Number is not in list
    
main()  #Starts main program
