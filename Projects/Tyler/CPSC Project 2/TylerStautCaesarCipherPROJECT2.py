#Author: Tyler R. Staut
#File Name: CaesarCipher.py
#Date: Nov 16, 2015
#Description: For encoding and Decoding

#-----LISTS-----#
alphabet = list("abcdefghijklmnopqrstuvwxyz")   #References for ciphering
alphabet_upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#---------------#


#----------DEFINITIONS----------#
def menu():   #Definition for the menu choices 
    print("The Caesar Cipher Program!")
    print("\n")
    print("Please choose from the following options: ")
    print("Option 1: Encrypt the file message.txt")
    print("Option 2: Decrypt the file cipher.txt")
    print("Option 3: Break the cipher")
    print("Option 4: Dictionary Attack the Cipher")
    print("Option 5: Quit")
    print("\n")
    
    choice = (input("Enter a choice: "))
    
    while int(choice) not in range(1,6): #Loop to keep the choices in bounds
        choice = int(input("Enter a choice: "))
    
    if int(choice) == 1: #Encrypt the file
        key = int(input("Enter the key for the cipher: "))
        while key not in range(1, 27):  #keep key in range loop
            key = int(input("Enter a proper key for the cipher: "))
            
        encryptFile(alphabet, key)
        
    elif int(choice) == 2:   #Decrypt the file
        key = int(input("Enter the key for the cipher: "))
        while key not in range(1, 27):
            key = int(input("Enter a proper key for the cipher: "))
            
        decryptFile(alphabet, key)
        
    elif int(choice) == 3:   #Brute force attack
        breakCipher(alphabet)
    elif int(choice) == 4:   #Dictionary attack Bonus
        dictAttack(alphabet)
    elif int(choice) == 5:   #Quit
        return 0    #Return to quit
    
    

def encryptFile(alphabet, key): #Definition to encrypt file
    myFile = open("message.txt")    #Opens file
    cipherFile = open("cipher.txt", "w")    #Opens file
    for line in myFile: #Splits up the lines in the file (Was going to have it read multiple lines for each part
        line.split()    #Splits up lines
    
    message = list(line)    #The message is the line, puts it in list
    count = 0   #Makes a count
    for char in message:    #Loop to get characters in the message and shift them, excluding special characters
        count += 1  
        if char in alphabet:    #Will shift the letter in the lower case alphabet
            message[count - 1] = alphabet[(alphabet.index(char) + key) % 26]
        elif char in alphabet_upper:    #Shifts letter in upper case alphabet
            message[count - 1] = alphabet_upper[(alphabet_upper.index(char) + key) % 26]

    
    
    newMessage = ''.join(message)   #Puts the new sentence back together
    cipherFile.write(newMessage)    #Puts it in a file
    
    print("Your encrypted message is: {}".format(newMessage))
    print("Also see in cipher.txt")
    
    cipherFile.close()  #Closes the file
    myFile.close()  #Closes the file

def decryptFile(alphabet, key): #Definition to decrypt file
    cipherFile = open("cipher.txt") #Opens file
    plainFile = open("plain.txt", "w")  #Opens file
    for line in cipherFile: #Loop to split up lines in file    
        line.split()
    
    message = list(line)    #Puts the lines in the message
    count = 0
    for char in message:    #For loop to go through message
        count += 1
        if char in alphabet:    #If it is in the lower case alphabet shift by key
            message[count - 1] = alphabet[(alphabet.index(char) - key) % 26]
        elif char in alphabet_upper:    #And upper case alphabet shift by key
            message[count - 1] = alphabet_upper[(alphabet_upper.index(char) - key) % 26]
    
    
    newMessage = ''.join(message)       #Join the new message  
    plainFile.write(newMessage) #Write it to file
    
    print("Your decrypted message is: {}".format(newMessage))   #Print it out
    print("Also see in plain.txt")
        
    cipherFile.close()  #Close the file
    plainFile.close()   #Close the file

def breakCipher(alphabet):  #Brute force attack definition
    cipherFile = open("cipher.txt")
    
    for key in range(26):   #For loop to do it for the 26 possible shifts
    
        for line in cipherFile: #Splits up the line
            line.split()
    
        message = list(line)    #Puts the line in the message
    
        count = 0
        for char in message:    #Goes through the message shifting the letters
            count += 1
            if char in alphabet:
                message[count - 1] = alphabet[(alphabet.index(char) - key) % 26]
                
            elif char in alphabet_upper:
                message[count - 1] = alphabet_upper[(alphabet_upper.index(char) - key) % 26]
        
        
        
        newMessage = ''.join(message)           #Puts the letters together
        
        print("Key = {}: {}".format(key, newMessage))   #Prints out all possible answers
                
    
    cipherFile.close()  #Close file
    

def dictAttack(alphabet):   #Dictionary attack definition
    attack = open("20k.txt")    #Opens the file of 20K English words
    cipherFile = open("cipher.txt") #Opens file
    
    sentencesToCheck = []   #List for sentences to check
    twentyKWords = []   #List to append 20k words to
    
    for key in range(26):   #Same as brute force but instead of printing out answers it stores them above in the sentenses to check list
    
        for line in cipherFile:
            line.split()
    
        message = list(line)
    
        count = 0
        for char in message:
            count += 1
            if char in alphabet:
                message[count - 1] = alphabet[(alphabet.index(char) - key) % 26]
                
            elif char in alphabet_upper:
                message[count - 1] = alphabet_upper[(alphabet_upper.index(char) - key) % 26]
        
        
        
        newMessage = ''.join(message)        
        
        sentencesToCheck.append(newMessage)
    
    #For checking amount of words in sentence to check if most words will work
    for line in cipherFile: #For loop to split up lines
        line.split()
    lengthChecker = line.split()    #Puts the words in a list to check length
    
    
    length = len(lengthChecker) #Gets Length of sentence
    #print(length)
    
    #For putting the 20k words into a list
    for line in attack: #For loop to get each and every word in the 20k word file in the word list
        line.split()
        twentyKWords.append(line.strip())
        
    #print(twentyKWords[12])
    #print(twentyKWords)
    answer = 0
    #For finding if the sentence works     
    for sentence in sentencesToCheck:   #For loop to get the different sentenses to check
        #print(sentence)
        count = 0
        for word in sentence.split():   #Checks each word in the sentence
            
            if word.lower() in twentyKWords:    #Since there could be weird caps throughout the sentence I used everything in lowercase
                #print(word)
                #UPDATE TO THE IF STATEMENT BELOW TO ALLOW FOR MULTIPLE SHORT SENTENCES WITH PUNCTUATION
                if count >= (length/3): #This is so that if maybe the user uses words not in the 20k word list but I doubt it
                                        #Also if the user puts in a 3 word message that contains names and a special character this will fix that
                    print("Based on our results, I believe this is the correct sentence: {}".format(sentence))
                    print("The key is: {}".format(sentencesToCheck.index(sentence)))
                    print("If you believe that somehow this is incorrect, please try Option 3 to see all possibilities.")
                    print('\n')
                    answer = 1
                    break
                count += 1
                #print(count)
    if answer == 0: #If it cant give a decent guess it will say this
        print("We could not determine the sentence or the key, try using the brute force attack (Option 3).")
        print('\n')
        
                
    
    cipherFile.close()  #Closes files
    attack.close()  
    
def main(): #Definition for main
    start = 1
    while start != 0:   #Keeps it looping until the program quits
        start = menu()

#-------------------------------#

#-----MAIN-----#
main()  #Starts the main program
#--------------#