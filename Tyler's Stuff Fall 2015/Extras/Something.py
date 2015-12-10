'''
Created on Sep 14, 2015

@author: tylerstaut
'''


n = int(input("Enter number of bags: "))

while True:
    if n < 0:
        print("Entered invalid number of bags.")
    elif n <= 2:
        print("Cost is $0")
    elif 2 < n <= 6:
        total_cost = 20 + (n-2)*40
        print("Your total cost is $", total_cost)
    elif n > 6:
        print("Cost is $180. But ", n - 6, " will need to be left.")
    break
