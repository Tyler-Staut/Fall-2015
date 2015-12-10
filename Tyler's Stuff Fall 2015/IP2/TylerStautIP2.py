#Author: Tyler R. Staut
#File Name: TylerStautIP2.py
#Date: Oct 30, 2015
#Description: IP2

#-----IMPORTS-----#
from random import randint
#-----------------#

#-----LISTS-----#
listOfBooks = []    #Its a list
#---------------#


#--------------------FUNCTIONS--------------------#
def printMenu():    #Definition that Prints the menu
    print("List all (L)")
    print("Add Book (A)")
    print("Number of books (N)")
    print("Random Book (R)")
    print("Quit (Q)")
    print("Bonus: Bulk Add (B)")
    
    choice = input("Enter a Choice: ")  #Choice
    while choice.upper() not in ("L", "A", "N", "R", "Q", "B"):     #Validation for choice
        choice = input("Enter a Valid Choice: ")
    return choice   #Returns choice ot main menu
    
def createListFromFile():   #Definition that Makes the file a list
    bookFile = open("books.txt")    #Opens file
    for book in bookFile:   #Gets book from file
        listOfBooks.append(book.strip())    #Appends books after striping off the newline but keeping spaces for the names to make them not look weird
        
    bookFile.close()    #Closes file
    return listOfBooks  #Returns updated list
    
def listAll():  #Definition for printing out everything
    print("List of all the Books: ")    #Just because
    for book in listOfBooks:
        print(book)     #Prints the book for each line wowie

def addBook(listOfBooks, bookName): #Definition for adding a book
    if bookName in listOfBooks: #If the book is already in the list it will get mad and tell you to not do that
        print("{} is already in the list.".format(bookName))
    else:
        listOfBooks.append(bookName)    #This will add the book
    return listOfBooks      #Returns new list

def numberOfBooks(listOfBooks):     #Definition for listing the books
    count = 0   #It didnt count yet
    for book in len(listOfBooks):   #For loop
        count += 1  #This is it counting
    return count    #It returns its last number after you make it slave over counting for you lol.

def randomBook(listOfBooks):    #Definition for random books
    randBook = randint(0, len(listOfBooks)) #Random num generator for picking random book
    return listOfBooks[randBook-1]  #returns a random book minus 1 because it will exceed the actual number of lines otherwise

def batchAdd(listOfBooks, stringThing):     #BONUS FUNCTION!!!!
    books = stringThing.split(',')  #TOO EASY LOL but this splits up input
    if books in listOfBooks:
        print("{} is already in the list.".format(stringThing)) #Found out this didnt actually work but it doesnt need to so oh well
    else:                                                       #Still adds the book so yeah it works
        listOfBooks.extend(books)   #Used extend here because thats how you do it, serously, thats how its done
    return listOfBooks  #Returns new list

def main():     #Main
    createListFromFile()
    choice = None
    while choice != 'Q':        #So porgram can quit
        choice = printMenu()
        
        if choice.upper() == 'L':   #Lists all books in list
            print("\n")
            listAll()
            print("\n")
            
        elif choice.upper() == 'A':     #Adds book
            print("\n")
            bookName = input("Enter a name of a book: ")
            print(addBook(listOfBooks, bookName))
            print("\n")
            
        elif choice.upper() == 'N':     #Prints number of books
            print("\n")
            print(numberOfBooks(listOfBooks))
            print("\n")
            
        elif choice.upper() == 'R':     #Prints out a random book
            print("\n")
            print(randomBook(listOfBooks))
            print("\n")
            
        elif choice.upper() == 'B':     #B for Bonus
            print('\n')
            stringThing = input("Enter your list of books separated by a comma: ")  #I did it
            print(batchAdd(listOfBooks, stringThing))   #This is the thing that i did to do it
#-------------------------------------------------#           
 
#-----MAIN-----#
main()      #Calls main function
#--------------#
    