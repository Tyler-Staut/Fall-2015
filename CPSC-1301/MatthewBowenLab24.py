#Name: Matthew Newton Bowen
#File Name: MatthewBowenLab24
#Date: 19 October 2015
#Description: Functions and Lists
def printList(anyList):
    if anyList == []: #If the list is empty, no entry
        print("no entry")
    elif anyList != []: #writes out the components of the list
        print("The components of your list are: ", end = " ")
        for x in anyList:
            print(x, end = " ")
def sumList(anyList):
    if anyList == []: #if your list is empty, then it will return 0
        print("0")
    else:
        print("\nThe sum of your list is %d" %sum(anyList)) #writes out the sum of the components
def avgList(anyList): 
    if len(anyList)==0: #If the length is 0, then it will return 0
        print("0")
    else:
        avg = (sum(anyList)) / (len(anyList)) #gets the average of the list's components
        print("The average value of your list is {0}".format(avg))
def maxList(anyList):
    if anyList == []: #if the list is empty, it will return 0
        print("0")
    elif anyList != []:
        max = anyList[0] #it will return the maximum value in the list
        for x in anyList:
            if x > max:
                max = x
    print("The maximum value in your list is %d" %max)
def minList(anyList):
    if anyList == []: #if the list is empty, return 0
        print("0")
    elif anyList != []:
        min = anyList[0]
        for x in anyList: #will return the minimum value in the list
            if x < min:
                min = x
    print("The minimum value in your list is %d" %min)
def isMember(anyList,anyNum):
    if anyList == []:
        print("0")
    elif anyList != []:
        if anyNum in anyList: #Will return true if the number is in the list, will return false if not
            return True
        else:
            return False
myList = [] #initiates list
print("Input integers to put into a list.")
inputNum = int(input("Enter an integer: ")) #beginning integer
while inputNum != 0: #loops to get list inputs until 0 is input
    myList.append(inputNum)
    inputNum = int(input("Enter an integer: "))
printList(myList) #Calls all the functions
sumList(myList)
avgList(myList)
maxList(myList)
minList(myList)
if myList == []: #If thelist is empty, return 0
        print("0")
elif myList != []:
    myNum = int(input("Input an integer to see if it is in your list: ")) #will return the values to verify if the number is in the list
    if isMember(myList,myNum) == True:
        print("Your list does contain %d" %myNum)
    elif isMember(myList,myNum) == False:
        print("Your list does not include %d" %myNum)