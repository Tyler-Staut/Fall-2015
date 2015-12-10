#Name: Matthew Newton Bowen
#File Name: MatthewBowenLab29
#Date: 06 November 2015
#Description: Data stuff

Matrix = [[1,2,3],[4,5,6],[7,8,9]] #2D List
for z in range(len(Matrix)):  #Will print out the 3 x 3 matrix
    for y in range(len(Matrix)):
        print(Matrix[z][y], end = ' ')
    print()
print("\nChoose a column and a row to display the value from.\n")
row = int(input("Which row? "))
while row > 3 or row < 1:  #Input validation
    row = int(input("Please choose a number between 1 and 3 for the row: "))
column = int(input("Which column? "))
while column > 3 or column < 1:  #Input validation
    column = int(input("Please choose a number between 1 and 3 for the column: "))
for x in range(1,len(Matrix)+1): #Gets the value from the list
    if row == x:
        if column == 1:
            print("The result is:", Matrix[x-1][0])
        if column == 2:
            print("The result is:", Matrix[x-1][1])
        if column == 3:
            print("The result is:", Matrix[x-1][2])
print("\n")
k = int(input("Please input a number to check if it is in the 2D list: "))
x = 0      #Will identify if the number is not in the list
for t in range(len(Matrix)):    #Checks to see if the number is in the list
    for s in range(len(Matrix)):
        if k == Matrix[t][s]:
            print("The value is located at row {0} and column {1}".format(t+1,s+1))
            x+=1 #Will identify if the number is in the list
if x == 0:
    print("The number {0} is not in this list.".format(k)) 
