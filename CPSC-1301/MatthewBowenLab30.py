#Name: Matthew Newton Bowen
#File Name: MatthewBowenLab30
#Date: 09 November 2015
#Description: Data stuff

distCities = [[0,983,787,714,1375,967],   #2D List
              [983,0,214,1102,1505,1723],
              [787,214,0,888,1549,1548],
              [714,1102,888,0,661,781],
              [1375,1505,1549,661,0,1426],
              [967,1723,1548,781,1426,0]]

def total(L):
    sumList = 0
    for x in range(len(L)):       #Making a sum for all the elements
        for y in range(len(L[x])):
            sumList += L[x][y]
    return sumList
    
def largestRowSum(L1):
    sumList1 = 0   #Initializing
    max = 0
    for r in range(len(L1)):
        for s in range(len(L1[r])): #gets the sum for each row
            sumList1 += L1[r][s]
        if sumList1 > max:    #If it's greater than the current max, store as the new max
            max = r+1
        sumList1 = 0
    return max

def smallestRowSum(L2):
    sumList2 = 0
    finalMin = sum(distCities[largestRowSum(L2)-1])
    minValue = sum(distCities[largestRowSum(L2)-1])   #Import the largest value as the initial minimum
    for t in range(len(L2)):
        for u in range(len(L2[t])):    #gets the sum of each row
            sumList2 += L2[t][u]
        if sumList2 < minValue:      #Stores as the new minimum if it's smaller than the current
            finalMin = t+1
        sumList2 = 0
    return finalMin

def largestColumnSum(L3):
    sumList3 = 0
    MaxV1 = 0
    for i in range(len(L3)):
        for j in range(len(L3[i])): #Gets the sum from each column rather than row
            sumList3 += L3[j][i]
        if sumList3 > MaxV1:      #Compares new max to the old max, and stores if it's larger
            MaxV1 = j
        sumList3 = 0
    return MaxV1

def main(L4):
    print("The total sum of all the elements of the list is {0}".format(total(L4)))   #Prints out the results
    print("The row with the largest sum is row {0}".format(largestRowSum(L4)))
    print("The row with the smallest sum is row {0}".format(smallestRowSum(L4)))
    print("The column with the largest sum is column {0}".format(largestColumnSum(L4)))
    
main(distCities)