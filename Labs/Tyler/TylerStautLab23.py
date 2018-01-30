#Author: Tyler R. Staut
#File Name: TylerStautLab23.py
#Date: 10/16/2015
#Description: Programming Challenge
from math import sqrt


x = int(input("Enter a Number: "))
sum = 0
for i in range(1, x + 1):
    sum += sqrt(i)
    
print(round(sum))
    
