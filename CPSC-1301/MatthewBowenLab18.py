#Name: Matthew Newton Bowen
#File Name: MatthewBowenLab18
#Date: 02 October 2015
#Description: Programming Challenge 2
for x in range(1,101):
    if(x % 3 == 0) and (x % 5 == 0): #Print FizzBuzz if number is a multiple of 3 and 5
        print("FizzBuzz")
    elif(x % 3 == 0): #Print Fizz if number is a multiple of 3 but not 5
        print("Fizz")
    elif(x % 5 == 0): #Print Buzz if number is a multiple of 5 but not 3
        print("Buzz")
    else: #For numbers not multiples of 3 or 5, just print the number.
        print(x)
        
        
        