#Name: Matthew Newton Bowen
#Date: 20 November 2015
#Title: Assignment 6
#Purpose: Ciphers 

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"        #All letters lower and capital


def encrypt(L,k):
    File1 = open("message.txt")         #Opening the files
    File2 = open("cipher.txt", "w")
    original = []
    newword = ""
    for line in File1:          #Splitting the line if necessary
        line.split()
        original.append(line)       #Build list from the lines of the text file
    letterList = []
    for x in range(len(original[0])):
        letterList.append(original[0][x])   #Build a list from the characters of the line
    for y in range(len(letterList)):        #Get the indexes of each letter
        for z in range(52):
            if L[z] == letterList[y]:
                letterList[y] = z
    for i in range(len(letterList)):    #Getting the shifted letters
        if letterList[i] in range(26):      #If the letter is lower case
            letterList[i] = letterList[i]+k
            letterList[i] = L[letterList[i]%26]     #Prevents out of range
        if letterList[i] in range(26,52):   #If the letter is capital
            letterList[i] = letterList[i]+k
            if letterList[i] > 51:      
                letterList[i] -= 26
            letterList[i] = L[letterList[i]%52]         #Prevents out of range
        newword += letterList[i]            #Builds new word
    print("Your encrypted message is:",newword)
    File2.write(newword)        #Writing the file
    print()
    print("Written to cipher.txt")
    File1.close()           #Closing files
    File2.close()
    

def decrypt(L,k):
    File3 = open("cipher.txt")              #Opening the files
    File4 = open("plain.txt","w")
    newMsg = []                     #Initiating the lists/string
    newLetterList = []
    newword1 = ""
    for row in File3:           #Splitting the row
        row.split()
        newMsg.append(row)
    for a in range(len(newMsg[0])):         #Building the list from the file
        newLetterList.append(newMsg[0][a])
    for b in range(len(newLetterList)):     #Getting the indexes of the letters
        for c in range(52):
            if L[c] == newLetterList[b]:
                newLetterList[b] = c
    for j in range(len(newLetterList)):         #Shifting the letters
        if newLetterList[j] in range(26):           #Shifting if lower case
            newLetterList[j] = newLetterList[j]-k
            newLetterList[j] = L[newLetterList[j]%26]
        if newLetterList[j] in range(26,52):        #Shifting if upper case
            newLetterList[j] = newLetterList[j]-k
            if newLetterList[j] < 26:       #Switched the signs since it's decrypting instead of encrypting
                newLetterList[j] += 26
            newLetterList[j] = L[newLetterList[j]%52]
        newword1 += newLetterList[j]            #Building the new shifted words
    print("Your decrypted message is:",newword1)
    File4.write(newword1)           #Writing to file
    print()
    print("Written to plain.txt")
    File3.close()               #Closing the files
    File4.close()
    
def allkeys(L):
    File5 = open("cipher.txt")          #Opening the files
    File6 = open("possibilities.txt","w")
    newest = []             #Initializing the lists and string
    ListofLetters = []
    newLetters = []
    lastList = []
    newword2 = ""
    for row in File5:       #Splitting the row
        row.split()
        newest.append(row)
    for d in range(len(newest[0])):         #building the list
        ListofLetters.append(newest[0][d])
    for f in range(len(ListofLetters)):
        for g in range(52):
            if L[g] == ListofLetters[f]:        #Getting the indexes of the words
                ListofLetters[f] = g
    newLetters = ListofLetters[:]       #Copying the list so it can be compared
    for n in range(1,27):
        newword2 = ""               #Clearing out the old words
        ListofLetters = newLetters[:]       #Making a fresh copy of the list
        for m in range(len(ListofLetters)):
            if ListofLetters[m] in range(26):
                ListofLetters[m] = ListofLetters[m]-n       #Shifting up the index once per iteration
                ListofLetters[m] = L[ListofLetters[m]%26]   #Using a loop of the decrypt, but for a different value each time
            if ListofLetters[m] in range(26,52):
                ListofLetters[m] = ListofLetters[m]-n
                if ListofLetters[m] < 26:
                    ListofLetters[m] += 26
                ListofLetters[m] = L[ListofLetters[m]%52]
            newword2 += ListofLetters[m]                    
        print("Key {0}) {1}".format(n,newword2))        #Printing out each string
        lastList.append(newword2)               #Adding the new string to a list
    for each in range(len(lastList)):
        File6.write("{0}\n".format(lastList[each]))     #writing each of them to the file on new lines
    print()
    print("Written to possibilities.txt")
    File5.close()           #Closing the files
    File6.close()
def menu():
    global choice
    print("Welcome to the cipher!")
    print("1) Encrypt the file message.txt")        #Options for the program
    print("2) Decrypt the file cipher.txt")
    print("3) Break the cipher")
    print("4) Quit")
    choice = input("Which would you like to do? ")
    while choice != "1" and choice != "2" and choice != "3" and choice != "4":
        print()                                     #Input validation
        choice = input("Please choose from one of the numbers on the menu.")
        
    if choice == "1":               #Runs the encrypt part of the program
        numShift = int(input("Please enter your key (1-26) "))
        if numShift > 26 or numShift < 1:
            numShift = int(input("Please enter a valid number for your key (1-26)"))
        encrypt(letters,numShift)
    
    if choice == "2":           #Runs the decrypt part of the program
        numShift = int(input("Please enter your key number (1-26) "))
        if numShift > 26 or numShift < 1:
            numShift = int(input("Please enter a valid number for your key (1-26)"))
        decrypt(letters,numShift)
        
    if choice == "3":           #Runs the version that prints using all keys
        allkeys(letters)
    if choice == "4":           #Quits the program
        print("Thank you!")
def main():
    go = 1                  #Initializes loop
    while go == 1:              #program loop
        print()
        menu()
        if choice == "4":       #Exit loop when user inputs 4
            go = 0
main()