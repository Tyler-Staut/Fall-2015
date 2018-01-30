#Name: Matthew Newton Bowen
#File Name: MatthewBowenLab23
#Date: 16 October 2015
#Description: Add Square Root Thing
import math
x = int(input("Enter a Value: "))
total = 0
for n in range(1,(x+1)):
    total = total + math.sqrt(n)
print(round(total))   