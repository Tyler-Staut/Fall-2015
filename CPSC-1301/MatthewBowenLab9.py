# Author:       Matthew Newton Bowen
# Program Name: MatthewBowenLab9.py
# Date:         September 11, 2015
# Purpose:      This program accepts the name and weight in pounds, height in
#                inches of a user and outputs the BMI for the user along with their name

Name = input("What is your name? ")
weight = float(input("How much do you weigh? (in pounds) "))
height = float(input("How tall are you? (in inches) "))

weightKilo = weight * 0.45359237 
heightMeters = height * 0.0254 
BMI = weightKilo/(heightMeters**2)

print(Name + ", your BMI is ", BMI)
