#Author: Tyler R. Staut
#File Name: TylerStautLab30.py
#Date: Nov 9, 2015
#Description: Lab 30

#----------LISTS----------#
distCities = [[0, 983, 787, 714, 1375, 967],
              [983, 0, 214, 1102, 1505, 1723],
              [787, 214, 0, 888, 1549, 1548],
              [714, 1102, 888, 0, 661, 781],
              [1375, 1505, 1549, 661, 0, 1426],
              [967, 1723, 1548, 781, 1426, 0]]  #Really big list that is not really that big
#-------------------------#

#----------FUNCTIONS----------#
def total(List):    #Definition for total of everything in list
    totalA = 0
    for L in range(len(List)):  #for loop
        for SL in range(len(List[L])):  #nested for loop
            totalA += List[L][SL]
    return totalA   #Returns the total amount
    
def largestRowSum(List):
    sumList = 0 #initiation variable
    largest = 0 #initiation variable
    for L in range(len(List)):  #Loop to go through list
        for SL in range(len(List[L])):  #Nested loop to go through nested list
            sumList += List[L][SL]
        if sumList > largest:   #if it is larger replace largest with the correct row
            largest = L + 1
        sumList = 0 #resets value for list
        
    return largest

def smallestRowSum(List):
    smallest = sum(distCities[largestRowSum(List)-1])   #used the total row sums to initiate smallest list
    lastMin = sum(distCities[largestRowSum(List)-1])    #did same here to only update this one when needed
    total = 0   #initiation variable
    for L in range(len(List)):  #loop to go through list
        for SL in range(len(List[L])):  #Nested loop to go through nested list
            total += List[L][SL]
        if total < smallest:    #if total is less than smallest replace the row
            lastMin = L + 1
        total = 0   #resets total value
          
    return lastMin  #return the last minimum value row
    
def largestColumnSum(List):
    total = 0
    largest = 0
    for L in range(len(List)):  #Loop to go through list
        for SL in range(len(List[L])):  #Nested list to go through nested list
            total += List[SL][L]
            if total > largest:
                largest = SL + 1    #used to get column using the sub list
            total = 0
        
    return largest  #returns largest column sum column
    
def main(disCities):    #Main function
    print('The total distance between the cities is: {}'.format(total(disCities)))
    print('The row with the largest sum is: {}'.format(largestRowSum(disCities)))
    print('The row with the smallest sum is: {}'.format(smallestRowSum(disCities)))
    print('The column with the largest sum is: {}'.format(largestColumnSum(disCities)))

#-----------------------------#

#-----MAIN-----#
main(distCities)    #Calls main function
#--------------#










