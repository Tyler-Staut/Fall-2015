#Author: Tyler R. Staut
#File Name: CaesarCipher.py
#Date: Nov 16, 2015
#Description: For encoding and Decoding

#-----LISTS-----#
alphabet = list("abcdefghijklmnopqrstuvwxyz")   #Reference for ciphering
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
        dictAttack(alphabet, )
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
        
        newMessage = ''.join(message)        
        
        print("Key = {}: {}".format(key, newMessage))
            
    
    cipherFile.close()
    

def dictAttack(alphabet, dictionary):
    
    sentencesToCheck = []
    
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
        
        newMessage = ''.join(message)        
        
        sentencesToCheck.append(newMessage)
            
    
    cipherFile.close()

def main():
    start = 1
    while start != 0:
        start = menu()

#-------------------------------#

main()