'''
Created on Sep 9, 2015

@author: Matt
'''
import math

print("Find all the info of your triangle!") 
print("All angles must be in degrees.")
print("You may choose SAS, SSS, ASA, or AAS")

def SAS(Side1, Angle1, Side2):
    areaSAS = (Side1*Side2*math.sin(Angle1))/2
    print(int(areaSAS))
    Angle2 = math.asin((Side1/Side2))
    Angle3 = math.pi - (Angle1 + Angle2)
    Side3 = Side2*math.sin(Angle1)

def SSS(Side1, Side2, Side3):
    s = (Side1 + Side2 + Side3)/2
    areaSSS = math.sqrt(s*(s - Side1)*(s - Side2)*(s - Side3))
    Angle1 = 
input("Which theorem would you like to use? ")

