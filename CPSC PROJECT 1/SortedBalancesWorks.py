#This program reads firstnames, last names, and balances from a file
#and puts them in three lists. It then prints the last names and the
#corresponding balances in a nice format
#Finally it prints the same list with balances sorted
#Author: CPSC 1301
#Date:10/30/2015


def print2Lists(list1,list2,titleWord): #list1 is for names and list2 is for balances
    print("\n\n")
    print("%-15s%8s"%(titleWord,"Balance"))    #print a title 
    print("------------------------------------------")
    for position,name in enumerate(list1):
        print("%-15s%8.2f"%(name,list2[position]))
    

#open the file
myfile=open("balances.txt")




#initilaize lists
firstNames=[]
lastNames=[]
balances=[]

# rea dthe file line by line and process each line as below
for line in myfile:
    if line=="\n": #do not process if the line is empty (continue to next line)
        continue
    fields=line.strip().split(",") #strip the line off any whitespace and split it by commas
    lastNames.append(fields[0]) #append the first field to lastNames
    firstNames.append(fields[1])#append the second filed to firstNames
    balances.append(float(fields[2])) #convert the third field to float and append to balances

input("Enter a key to see the list of last names and balances") 

print2Lists(lastNames,balances,"Last Name")

input("Enter a key to see the list of first names and balances") 
print2Lists(firstNames,balances,"First Name")




input("Enter a key to see the list with sorted balances:") #wait for user input

sortedBalances=sorted(balances) #sort the balances (leave the original list intact)
print("\n\n")
print("%-15s%8s"%("Last Name","Balance"))
print("------------------------------------------")
for balance in sortedBalances:
    k=balances.index(balance)
    name=lastNames[k]
    print("%-15s%8.2f"%(name,balance))
    balances.remove(balance)
    lastNames.remove(name)
    
##input("Enter a key to see the lists with oroginal order:") #wait for user input
##
##print2Lists(lastNames,balances)
