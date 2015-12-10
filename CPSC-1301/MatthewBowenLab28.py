#Name: Matthew Newton Bowen
#File Name: MatthewBowenLab28
#Date: 02 November 2015
#Description: Palindrome checker

strList = []                #Initializations
newList = []
testList = []
begin = "yes"

def reverseString(string):
    length = len(string)    #Gets length of the string
    z = ""                  #initialize
    L1 = length
    for x in range(length): #build list from the string
        strList.append(string[x])
    for x in range(length): #reverses the string
        newList.append(strList[length-1])
        length = length - 1
    for letter in range(L1): # builds the reverse of the word
        z = z + newList[letter]
    return z                #returns the reverse word

def reverseString2(string): 
    testList = string[::-1] #splits the list and put it in reverse order
    return testList         #returns the reverse word
    
    
def main():
    string = input("Input a string: ") #takes input
    print(" ")
    string1 = string
    string = string.lower()             #Makes all the letters lower case 
    string = string.replace(" ", "")    #replace the spaces with nothing
    reverseString2(string)
    if string == reverseString2(string):    #If the string is the same as the reverse, then it's a palindrome
        print("{} is a palindrome.".format(string1))
    else:
        print("{} is not a palindrome.".format(string1))
    

while begin == "yes": #loop
    main()
    begin = input("Would you like to use this tool again? (yes/no): ")
print("Thank you for using!")   #Thank you