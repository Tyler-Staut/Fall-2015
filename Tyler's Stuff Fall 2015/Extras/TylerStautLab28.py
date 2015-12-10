#Author: Tyler R. Staut
#File Name: TylerStautLab28.py
#Date: Nov 2, 2015
#Description: palindrome checker thing

#-----LISTS-----#
letterList = []
letterList2 = []
wordList = []
#---------------#



#----------FUNCTIONS----------#
def reverseString(word):
    word2 = word.replace(' ','')    #Gets rid of those pesky spaces
    for letter in word2.lower():    #Puts letters from word in list
        letterList.append(letter)
    
    for letter in word2.lower():    #Puts letters from word in list
        letterList2.append(letter)
    
    letterList2.reverse()   #Reverses the list
    

    if letterList2 == letterList:
        print("{}, is a palindrome.".format(word))  #I like this formatting
        
    else:
        print("{}, is not a palindrome.".format(word))  #I really like this way more than the % stuff
    
def reverseString2(word):
    word2 = word.replace(' ','')    #Gets rid of those pesky spaces
    wordList = word2[::-1]  #Uses the split thingy that we were supposed to use
    
    if wordList.lower() == word2.lower():   #Checks the words
        print("{}, is a palindrome.".format(word))
        
    else:
        print("{}, is not a palindrome.".format(word))
    
        
           
def main():
    #Did not get rid of white space here because I wanted it to tell the user what they entered
    #I used a replace function in the definitions because it seemed easier for me. 
    start = 1 #Initiates the loop
    while start != 0:
        reverseString2(input("Enter a word you would like to have checked: "))  #Used reverse string 2 for this one though reverse string would work too.
        start = int(input("1 Continue - 0 Exit: "))
        while start not in (1,2):   #validation for correct answer
            start = int(input("1 Continue - 0 Exit: "))
main() # Starts program

