#Author: Tyler R. Staut
#File Name: TylerStautLab8
#Date: 9/4/2015
#Description: Converts fractions into a mixed fraction

#--------------------VARIABLES-------------------------
numerator = int(input("Please enter your Numerator: "))         #Numerator
denominator = int(input("Please enter your Denominator: "))     #Denominator

#usrInput = numerator/denominator                               #What the user put in and not actually used because not needed

newNumerator = numerator % denominator                          #The numerator after the fraction is simplified and the coefficient is pulled out
coefficient = numerator // denominator                          #The number that goes before the fraction

#mixedFraction = int((newNumerator / denominator)) - NOT ACTUALLT USED
#------------------------------------------------------

#--------------------OUTPUT----------------------------
print(numerator, "/", denominator, "is equal to: ",
      coefficient, newNumerator, "/", denominator)        #This prints the output
#------------------------------------------------------
