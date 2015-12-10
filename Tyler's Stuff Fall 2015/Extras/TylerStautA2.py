# Purpose: This program calculates and displays the wind 
# chill temperature index for given temperatures and wind 
# speed
# Author: Tyler R. Staut
# Date: <date of completion>

#--------------------IMPORTS----------------------
#import math        #Imported math so that I can later use to round wctIndex answer to nearest whole number
                    #---DID NOT NEED---
                    

#-------------------------------------------------

#--------------------PART A-----------------------
#Data Set 1
airTemp1 = float(10.0)
airSpeed1 = float(15)

#Data Set 2
airTemp2 = float(0.0)
airSpeed2 = float(25)

#Data Set 3
airTemp3 = float(-10.0)
airSpeed3 = float(35)

#Starting Variables
airSpeed = 0
airTemp = 0

x = int(input("How many places do you want the answers rounded to: "))    #Added this so that the user can define how many 
                                                                            #places they wanted their answers to be accurate to.
                                                                            #Added it just in case.

#Defines the Function used to calculate WindChill
def windchill(airTemp, airSpeed):
    wctIndex = float(35.74 + (0.6215 * airTemp) -                  # Equation used to calculate windchill.
                      (35.75 * (airSpeed ** 0.16)) +                # Defined it as a function so I dont have to keep
                      (0.4275 * airTemp * (airSpeed ** 0.16)))      # typing it over and over again. This is like version 12 for me
    print (airTemp, "degrees F and",  airSpeed, "MPH")
    print("The Wind Chill Temperature Index is: ", str(round(wctIndex,x)), "degrees F\n")

    # These print out the info for Part A
print("\nExamples: ")
#Data Set 1
airSpeed=airSpeed1
airTemp=airTemp1
windchill(airTemp, airSpeed)

#Data Set 2
airSpeed=airSpeed2
airTemp=airTemp2
windchill(airTemp, airSpeed)

#Data Set 3
airSpeed=airSpeed3
airTemp=airTemp3
windchill(airTemp, airSpeed)
print("-------------------------------------------")        #Added this to section off examples from user input.
#-------------------------------------------------

#--------------------Part B-----------------------
airTemp = float(input("What is the Air Temperature: "))
airSpeed = float(input("What is the Air Speed: "))
print("\n")
windchill(airTemp, airSpeed)
#-------------------------------------------------