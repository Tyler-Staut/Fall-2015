'''
Created on Sep 21, 2015

@author: tylerstaut
'''

num = int(input("Enter a Number: "))

def set1():
    if ((num % 2) and (num % 3)) == 0:
        print(num, "can be divided by 2 and 3")
    else:
        print(num, "is not divisible by 2 and 3")
    
def set2():
    if ((num % 2) or (num % 3)) == 0:
        print(num, "can be divided by 2 or 3")
    else:
        print(num, "is not divisible by 2 or 3")
    
    


set1()
set2()