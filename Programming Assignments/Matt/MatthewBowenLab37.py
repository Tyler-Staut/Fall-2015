#Name: Matthew Newton Bowen
#File Name: MatthewBowenLab37
#Date: 2 December 2015
#Description: DIGITSSSSS

def sumDigits(number):
    total = 0                       #Initialize total
    if number >= 1 and number <= 9: #If number is between 1 and 9
        return number               #Return this number
    else:
        total+= (number%10) + (sumDigits(number//10))   #Take the remainder and add the function of the other part to it. 
        return total                #Returns this total
    
thing = int(input("Number: "))          #Prints
print(sumDigits(thing))