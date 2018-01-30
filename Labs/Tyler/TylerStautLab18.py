#Author: Tyler R. Staut
#File Name: TylerStautLab18.py
#Date: 10/2/2015
#Description: Fizz Buzz!

#----------PROGRAM----------
for i in range(1, 100):     #The Main Range to go through
    if (i % 3 == 0) and (i % 5 == 0):       #If it does both do FizzBuzz
        print('FizzBuzz')
    elif (i % 3 == 0):      #Else if every three do Fizz
        print('Fizz')
    elif (i % 5 == 0):      #Else if every five do Buzz
        print('Buzz')   
    else:                   #Else just print i
        print(i)
#---------------------------    

        