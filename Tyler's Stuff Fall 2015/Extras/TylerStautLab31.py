#Author: Tyler R. Staut
#File Name: TylerStautLab31.py
#Date: Nov 11, 2015
#Description: Lab 31

#----------FUNCTIONS----------#

def replace_word(sentence, target, replacement):    #This will replce a word hopefully
    newSentence = sentence.split()  #Makes sentence a list and splits it up all fancy like
    count = 0   #Initiates count
    for word in newSentence:    #Goes through list
        count += 1  #Whilst counting
        if word.lower() == target.lower():  #in search for the target word
            newSentence.remove(word)    #Gets rid of that word because we dont like it
            newSentence.insert(count - 1, replacement)  #replaces it with replacement
    
    newSentence = ' '.join(newSentence) #Rejoins sentence
    return newSentence  #returns sentence
    
def reverseSentence(sentence):  #This will reverse the sentence
    newSentence = sentence.split()  #this will split up the sentence into a list
    newSentence.reverse()   #This will reverse it, hence the reverse
    newSentence = ' '.join(newSentence) #Joins the sentence together
    return newSentence  #Returns new sentence
    
def main(): #this is the main and calls everything
    #Part 1
    print(replace_word(input("Enter a string: "),
                        input("Enter the target word: "),
                         input("Enter the replacement word: ")))    #Inputs for the thing to do the thing, being specific here because im lazy
    
    #Part 2
    print(reverseSentence(input("Enter a string you want to have reversed: "))) #also does the thing for the definition, again lazy
    
    #Part 3
    str = 'X-DSPAM-Confidence: 0.8475'  #Really not sure what this is supposed to do for the program but it works and you want it so its here??
    x = str.find(':') + 1 #Plus 1 so that it doesnt take in the colon
    newStr = str[x:]    #this gets the rest of the string so it can be converted probably in the next line
    print(float(newStr))    #Yeah i converted it here and it was great, also it prints the number thing
    
#-----------------------------#

#-----MAIN-----#
main()  #Calls the main function
#--------------#
        



