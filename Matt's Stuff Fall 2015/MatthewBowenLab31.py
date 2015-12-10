#Name: Matthew Newton Bowen
#File Name: MatthewBowenLab31
#Date: 11 November 2015
#Description: String Ops

def replace_word(sentence, target, replacement):
    S = sentence.split()       #Splits up the sentence
    if target[-1] == "." or target[-1] == ",":   #gets rid of punctuation
        target.strip()
    t = 0
    for x in S:  #Gives the index of the target
        if x == target:
            t = S.index(x)
    S.remove(target) #removes the target
    S.insert(t,replacement)   #Inserts the replacement at the index of the former target
    T = ""
    for z in S:    #Builds the string back
        T = T+" "+z
    return T

def reverse_sentence(sentence):
    R =sentence.split()     #Splits the sentence
    R.reverse()             #reverses the elements
    T = ""                  #rebuilds the string
    for i in R:
        T = T+" "+i
    return T
    
def StringOps():
    str = 'X-DSPAM-Confidence: 0.8475'
    A = str.find(":")+1
    NewS = str[A:]
    print(float(NewS))
    
def main():
    Sent = input("What sentence would you like to use? ")           #Gets inputs
    Target = input("Which word would you like to replace? ")
    while Target not in Sent:
        Target = input("Please choose a word from the sentence to replace. ")
    Replacement = input("What would you like to replace it with? ")
    print(replace_word(Sent, Target, Replacement))
    Sent1 = input("What sentence would you like reversed? ")
    print(reverse_sentence(Sent1))
    StringOps()
    
main()