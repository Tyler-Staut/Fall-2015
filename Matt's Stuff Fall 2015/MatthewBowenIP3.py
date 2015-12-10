#Name: Matthew Newton Bowen
#File Name: MatthewBowenIP3
#Date: 20 November 2015
#Description: Independent Programming III


#-----------------Lists-----------------#
scores = [[203,122,345,89,310,267,199,172],
          [198,0,365,123,79,256,168,288],
          [325,187,145,324,265,102,136,45],
          [111,402,212,89,197,301,0,158],
          [268,165,121,346,99,147,215,166],
          [0,192,243,368,149,256,244,91]]

names = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5" ,"Player 6"]

scorelabels = ["Score 1", "Score 2", "Score 3", "Score 4", "Score 5", "Score 6", "Score 7", "Score 8"]

#---------------------------------------#
def TablePrint(L1,L2,L3):
    print("         ", end = " ")
    for x in range(len(L3)):
        print(L3[x] + " ", end = " ")
    print()
    for z in range(6):
        print(L2[z]+ " ", end = " ")
        for y in range(len(L1[0])):
            if len(str(L1[z][y])) == 3:
                print(str(L1[z][y]) + "     ", end = " ")
            if len(str(L1[z][y])) == 2:
                print(str(L1[z][y]) + "      ", end = " ")
            if len(str(L1[z][y])) == 1:
                print(str(L1[z][y]) + "       ", end = " ")
            
        print()            
        
def total(L4):
    sumlist = 0
    for v in range(len(L4)):
        for w in range(len(L4[v])):
            sumlist += L4[v][w]
    return sumlist
    
def playertotal(L5, name):
    if "1" in name:
        sumlist1 = 0
        for r in range(len(L5[0])):
            sumlist1 += L5[0][r]   
        return sumlist1
    if "2" in name:
        sumlist2 = 0
        for r in range(len(L5[1])):
            sumlist2 += L5[1][r]   
        return sumlist2
    if "3" in name:
        sumlist3 = 0
        for r in range(len(L5[2])):
            sumlist3 += L5[2][r]   
        return sumlist3
    if "4" in name:
        sumlist4 = 0
        for r in range(len(L5[3])):
            sumlist4 += L5[3][r]   
        return sumlist4
    if "5" in name:
        sumlist5 = 0
        for r in range(len(L5[4])):
            sumlist5 += L5[4][r]   
        return sumlist5
    if "6" in name:
        sumlist6 = 0
        for r in range(len(L5[5])):
            sumlist6 += L5[5][r]   
        return sumlist6

def scorecolumntotal(L5, column):
    if "1" in column:
        sumlist1 = 0
        for r in range(6):
            sumlist1 += L5[r][0] 
        return sumlist1
    if "2" in column:
        sumlist2 = 0
        for r in range(6):
            sumlist2 += L5[r][1]   
        return sumlist2
    if "3" in column:
        sumlist3 = 0
        for r in range(6):
            sumlist3 += L5[r][2]   
        return sumlist3
    if "4" in column:
        sumlist4 = 0
        for r in range(6):
            sumlist4 += L5[r][3]   
        return sumlist4
    if "5" in column:
        sumlist5 = 0
        for r in range(6):
            sumlist5 += L5[r][4]   
        return sumlist5
    if "6" in column:
        sumlist6 = 0
        for r in range(6):
            sumlist6 += L5[r][5]   
        return sumlist6
    if "7" in column:
        sumlist7 = 0
        for r in range(6):
            sumlist7 += L5[r][6]   
        return sumlist7
    if "8" in column:
        sumlist8 = 0
        for r in range(6):
            sumlist8 += L5[r][7]   
        return sumlist8
    
def printmenu():
    global choice
    TablePrint(scores, names, scorelabels)
    print()
    print("Select an option from below:")
    print("1) Total sum of all scores")
    print("2) Players total score")
    print("3) Column score")
    print("4) Quit")
    print()
    choice = int(input("Which option? "))
    if choice == 1:
        print(total(scores))
    if choice == 2:
        name = input("Which player? ")
        print(playertotal(scores, str(name)))
    if choice == 3:
        column = input("Which column? ")
        print(scorecolumntotal(scores, str(column)))
    if choice == 4:
        print("Thank you!")
    yes1 = input("Would you like to go again? (y/n)")
    if yes1 == "n":
        choice = 4
        

def main():
    go = 0
    while go == 0:
        printmenu()
        if choice == 4:
            go = 1
main()