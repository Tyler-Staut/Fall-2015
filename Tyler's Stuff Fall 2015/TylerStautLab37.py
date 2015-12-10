#Author: Tyler R. Staut
#File Name: TylerStautLab37.py
#Date: Dec 2, 2015
#Description: Lab 37 NUMBERSSSSSSS



def sumDigit(number):
    total = 0
    if number in range(0,10):   #If the number is within this range just return that number because that makes sense.
        return number   #This is where it returns
#     elif number >= 100:    #This was a failure please ignore
#         return sumDigit(number // 10)
    else:   #Else go through the number without a loop but recursiely to add the entire sum of its parts
        total += (number % 10) + sumDigit(number // 10) #Total is updated, add the ones digit to the rest by using // to get the next parts to add together. This explanition may be bad, i just want to go and eat.
        return total    #Returns the total

user_input = int(input("Enter a number to get the sum of its digits: "))    #Input from the user
answer = (sumDigit(user_input)) #gets answer for output
print("The sum of the digits of the integer you entered is: {}".format(answer)) #Output with the answer


