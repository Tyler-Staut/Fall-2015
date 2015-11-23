#Author: Tyler R. Staut
#File Name: CaesarCipher.py
#Date: Nov 16, 2015
#Description: For encoding and Decoding

#-----LISTS-----#
alphabet = list("abcdefghijklmnopqrstuvwxyz")   #Reference for ciphering
alphabet_upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#---------------#


#----------DEFINITIONS----------#
def menu():   #Definition for the menu choices 
    
    print("\n")
    print("Option 1: Encrypt the file message.txt")
    print("Option 2: Decrypt the file cipher.txt")
    print("Option 3: Break the cipher")
    #print("Option 4: Dictionary Attack Cipher")
    print("Option 5: Quit")
    print("\n")
    
    choice = int(input("Enter a choice: "))
    while choice not in range(1,6):
        choice = int(input("Enter a choice: "))
    
    if choice == 1:
        key = int(input("Enter the key for the cipher: "))
        while key not in range(1, 27):
            key = int(input("Enter the key for the cipher: "))
            
        encryptFile(alphabet, key)
        
    elif choice == 2:
        key = int(input("Enter the key for the cipher: "))
        while key not in range(1, 27):
            key = int(input("Enter the key for the cipher: "))
            
        decryptFile(alphabet, key)
        
    elif choice == 3:
        breakCipher(alphabet)
    elif choice == 4:
        dictAttack(alphabet)
    elif choice == 5:
        return 0
    
    

def encryptFile(alphabet, key):
    myFile = open("message.txt")
    cipherFile = open("cipher.txt", "w")
    for line in myFile:
        line.split()
    
    message = list(line)
    count = 0
    for char in message:
        count += 1
        if char in alphabet:
            message[count - 1] = alphabet[(alphabet.index(char) + key) % 26]
        elif char in alphabet_upper:
            message[count - 1] = alphabet_upper[(alphabet_upper.index(char) + key) % 26]

    
    
    newMessage = ''.join(message)
    cipherFile.write(newMessage)
    
    cipherFile.close()
    myFile.close()

def decryptFile(alphabet, key):
    cipherFile = open("cipher.txt")
    plainFile = open("plain.txt", "w")
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
    print(newMessage)
    
    plainFile.write(newMessage)
    
    cipherFile.close()
    plainFile.close()

def breakCipher(alphabet):
    cipherFile = open("cipher.txt")
    
    for key in range(26):
    
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
        
        print("Key = {}: {}".format(key, newMessage))
            
    
    cipherFile.close()
    

def dictAttack(alphabet):
    attack = open("20k.txt")
    cipherFile = open("cipher.txt")
    
    sentencesToCheck = []
    twentyKWords = []
    
    for key in range(26):
    
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
    for line in cipherFile:
        line.split()
    lengthChecker = line.split()
    
    
    length = len(lengthChecker) #Length of sentence
    #print(length)
    
    #For putting the 20k words into a list
    for line in attack:
        line.split()
        twentyKWords.append(line.strip())
        
    #print(twentyKWords[12])
    #print(twentyKWords)
    answer = 0
    #For finding if the sentence works     
    for sentence in sentencesToCheck:
        #print(sentence)
        count = 0
        for word in sentence.split():
            
            if word.lower() in twentyKWords:
                #print(word)
                if count >= length - 2:
                    print("Based on our results, I believe this is the correct sentence: {}".format(sentence))
                    print("The key is: {}".format(sentencesToCheck.index(sentence)))
                    answer = 1
                count += 1
    if answer == 0:
        print("We could not determine the sentence or the key, try using the brute force attack (Option 3).")
        
                
    
    cipherFile.close()
    attack.close()
    
def main():
    start = 1
    while start != 0:
        start = menu()

#-------------------------------#

#-----MAIN-----#
main()
#--------------#