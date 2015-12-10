'''
Created on Sep 18, 2015

@author: Tyler Staut
'''

num = int(input("Enter a number: "))

if num % 10 == 2:
    print("True")
elif num // 10 == 2:
    print("True")
elif num == 2:
    print("True")
elif num == 8:
    print("True")
else:
    print("False")