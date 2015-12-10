# Author: Thomas Lin
# File Name: date_checker.py
# Description: Write a program that reads a date from numeric form
# Date: September 17, 2015

month = [' ', 'January', 'Feburary', 'March',
          'April', 'May', 'June', 'July', 'August',
           'September', 'October', 'November', 'December']

y=int(input("Enter a year: "))

while True:
    m=int(input("Enter a month when January=1 and December=12: "))
    if 1<=m<=12:
        break
    print("Please enter a valid number.")

while True:
    d=int(input("Enter a day of the month: "))
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if 1<=d<=31:
            break
        print("Please pick a value from 1-31.")
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if 1<=d<=30:
            break
        print("Please pick a value from 1-30.")
    elif m == 2:
        if y//4 != y/4:
            if 1<=d<=28:
                break
            print("Please pick a value from 1-28")
        elif y//4 == y/4:
            if 1<=d<=29:
                break
            print("Please pick a value from 1-29")


print("The date you choose:", month[m], d,',', y)
