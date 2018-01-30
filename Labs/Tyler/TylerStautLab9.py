# Author:       Tyler R. Staut 
# Program Name:  BMI.py
# Date:         Sep 10, 2015
# Purpose:      This program accepts the name and weight in pounds, height in
#                inches of a user and outputs the BMI for the user along with their 
#                name

#----------VARIABLES----------
weightLb = 0
heightIn = 0
#-----------------------------

#----------DESCRIBES BMI VALUES--------------------------------------------
print('''Underweight = <18.5
Normal weight = 18.5–24.9 
Overweight = 25–29.9 
Obesity = BMI of 30 or greater\n''')
#--------------------------------------------------------------------------

#--------------------INPUTS------------------------------------------------
weightKg = float(input("What is your weight in Pounds: ")) * 0.45359237     #Used to calculate weight in Kg
heightCm = float(input("What is your height in Inches: ")) * 0.0254         #Used to calculate height in Meters
#--------------------------------------------------------------------------

#-------------BMI FORMULA---------------
BMI = round(weightKg / (heightCm**2))
#---------------------------------------


print("Your BMI is", BMI)       #Prints the result of your BMI