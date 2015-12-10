#Name: Matthew N. Bowen
#Date: 25 September, 2015
#Title: MatthewBowenIP2 (Independent Programming 2)
#Purpose: Reading List
import random
readingList = []
def printMenu():
    print(" List All (L) ")
    print(" Add Book (A) ")
    print(" Number of Books (N) ")
    print(" Random Book (R) ")
    print(" Quit (Q) ")
    choice = input("Which choice would you like to do? ")
    while choice != 'L' and choice != 'A' and choice != 'N' and choice != 'R' and choice != 'Q':
        choice = input("Please choose a letter from above (L, A, N, R, or Q): ")
    if choice == 'L' or choice == 'A' or choice == 'N' or choice == 'R' or choice == 'Q':
        if choice == 'L':
            return 'L'
        elif choice == 'A':
            return 'A'
        elif choice == 'N':
            return 'N'
        elif choice == 'R':
            return 'R'
        elif choice == 'Q':
            return 'Q'

def createListFromFile():
    Books = open("C://books.txt")    
    for line in Books:
        line.strip(" ")
        readingList.append(line)
    Books.close()
    return readingList

def listAll(L1):
    for x in range(len(L1)):
        print(L1[x])


def addBook(L2, b):
    if b in L2:
        print("This book is already in the list.\n")
    else:
        L2.append(b)
    return L2

def numberOfBooks(L3):
    return len(L3)

def randomBook(L4):
    y = random.randint(0,5)
    return L4[y]

def main():
    A = "I"
    while A != 'Q':
        A = printMenu()
        if A == 'L':
            print(" ")
            listAll(createListFromFile())
            print(" ")
        elif A == 'A':
            print(" ")
            B = input("What book would you like to add?") 
            print(addBook(createListFromFile(), B))
            print(" ")
        elif A == 'N':
            print(" ")
            print(numberOfBooks(createListFromFile()))
            print(" ")
        elif A == 'R':
            print(" ")
            print(randomBook(createListFromFile()))
            print(" ")
    print("Thank you for using!")
    
main()