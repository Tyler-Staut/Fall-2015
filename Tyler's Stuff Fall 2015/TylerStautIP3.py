#Author: Tyler R. Staut
#File Name: TylerStautIP3.py
#Date: Nov 20, 2015
#Description: IP3

#----------LISTS----------#
scores = [[203,122,345,89,310,267,199,172],
          [198,0,365,123,79,256,168,288],
          [325,187,145,324,265,102,136,45],
          [111,402,212,89,197,301,0,158],
          [268,165,121,346,99,147,215,166],
          [0,192,243,368,149,256,244,91]]

#Yes I know I could have used a for loop to do this, I forgot.
playerNames = ['Player 1','Player 2','Player 3','Player 4','Player 5','Player 6']
scoresAndNames = []
columnLabels = ['Score 1','Score 2','Score 3','Score 4','Score 5','Score 6','Score 7','Score 8']
#-------------------------#
for player in range(len(playerNames)):
    scoresAndNames.append([playerNames[player], scores[player]])


#for player in range(len(playerNames)):
    #print(scoresAndNames[player][0], scoresAndNames[player][1])

def printTable(twoDList):   #Definition to print table
    print('          ', end='')
    for i in range(len(columnLabels)):
        print(columnLabels[i], end=' | ')
    print()
    count = 0   #Sets up count
    for num in range(len(twoDList)):    #Loop
        count += 1  #Adds one to count
        
        print("%-4s | %-4s" % (twoDList[num][0], (twoDList[num][1]))) 
        
        if count % 8 == 0: #Count thingie to make new line
            print('\n') #Empty print for new line


def total(List):
    totalA = 0
    for L in range(len(List)):  #for loop
        for SL in range(len(List[L])):  #nested for loop
            totalA += List[L][SL]
    return totalA   #Returns the total amount

def playerTotal(twoDList, name):
    
    total = 0
    for item in range(len(twoDList)):
        total += twoDList[name][item]
    return total   
        
def scoreColumnTotal(twoDList, column):
    total = 0
    for score in range(6):
        total += twoDList[score][column-1]
    return total

def printMenu():
    print("1. Give total of scores.")
    print("2. Total of player scores.")
    print('3. Total of column scores.')
    print('4. Quit')
    
    choice = int(input("Enter your choice(1-3): "))
    if choice == 1:
        return 1
    elif choice == 2:
        return 2
    elif choice == 3:
        return 3
    elif choice == 4:
        return 4

def main():
    printTable(scoresAndNames)
    print()
    choice = 0
    while choice != 4:
        
        choice = printMenu()
        if choice == 1:
            print("The total of all scores is: ", total(scores))
        elif choice == 2:
            name = input("Enter a name: ")
            print(playerTotal(scores, name))
        elif choice == 3:
            column = int(input("Enter column number: "))
            print("The Column total is: ", scoreColumnTotal(scores, column))
        elif choice == 4:
            choice = 4
    
main()
