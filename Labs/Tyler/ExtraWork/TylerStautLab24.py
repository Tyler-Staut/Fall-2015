#Author: Tyler R. Staut
#File Name: TylerStautLab24.py
#Date: 10/19/2015
#Description: Functions and Lists



#-----LISTS-----
anyList = []
myList = []
#---------------

#----------CLASS WITH DEFS----------
class listThing():
    def printList(self, anyList):     #Def for printing list
        if anyList == []:
            print("No Entries.")
        else:
            print("The list contains: {0}".format(anyList))  #Prints out list
                
    def sumList(self, anyList):       #Def for sum of list
        if sum(anyList) == 0:
            print("0")
        else:
            print("The sum of the list is: {0}".format(sum(anyList)))    #Prints sum of list
            
    def avgList(self, anyList):    #Def for avg of list   
        avg = (sum(anyList)) / (len(anyList))   #Calculates average of list
        if len(anyList) == 0:
            print("0")
        else:
            print("The average of the list is: {0}".format(avg)) #Prints average of list
            
    def maxList(self, anyList):   #Def for max of list
        listMax = anyList[0]
        for i in anyList:   #Finds max
            if i > listMax: 
                listMax = i
        print("The maximum of the list is: {0}".format(listMax)) #Prints max
                        
    
    def minList(self, anyList):   #Def for min of list
        minimum = anyList[0]
        for i in anyList:   #Finds min
            if i < minimum:
                minimum = i
        print("The minimum of the list is: {0}".format(minimum)) #Prints min
        
    def isMember(self, anyList, anyNum):      #Def for looking for user_input in list
        if len(anyList) == 0:   #No numbers were entered into list
            return False
        elif anyNum in anyList: #Found user_input in list
            return True
        elif anyNum not in anyList: #User_input is not in list
            return False
    
    def inputs(self): #Def for geting the numbers to put into the list
        user_input = int(input("Please enter a number: "))
        myList.append(user_input)
        while (user_input != 0) or (user_input != ' '):  #Loop to add more numbers
            user_input = int(input("Please enter a number: "))
            if user_input == 0:
                break
            myList.append(user_input)
#-------------------------------
    
T = listThing()     #Sets the variable T to the class i set so it is easier to call to in the program multiple times.
    
def main():     #Main calls all functions in order
    print("Enter numbers you would like put into a list. Enter 0 to when you are done.")
    
    T.inputs()    #Calls program inputs
    print("\n") #Used to seperate parts of program
    T.printList(myList)   #Prints inputs
    print("\n") #Used to seperate parts of program
    T.sumList(myList)     #Prints sum of list
    print("\n") #Used to seperate parts of program
    T.avgList(myList)     #Prints average of list
    print("\n") #Used to seperate parts of program
    T.maxList(myList)     #Prints the max of the list 
    print("\n") #Used to seperate parts of program   
    T.minList(myList)     #Prints the min of the list
    print("\n") #Used to seperate parts of program
    
    anyNum = int(input("Enter an Integer to check if it is in the list: "))
    if T.isMember(myList, anyNum) == True:    #Checks if num in in list
        print("The integer you entered, {0}, is in the list.".format(anyNum))   #Used .format because it is better. It does not round automatically and I cant believe I forgot about it after all these years. This program could also benifit from using a class but people will probably not understand that.
    else:
        print("The integer you entered, {0}, is not in the list.".format(anyNum))
#-------------------------------
  
#-----START PROGRAM-----      
main()
#-----------------------

    

    