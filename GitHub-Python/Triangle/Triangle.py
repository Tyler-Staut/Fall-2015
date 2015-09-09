'''
Created on Sep 9, 2015

@author: Matt
'''
import math

print("Find all the info of your triangle!") 
print("You may choose from SAS, SSS, ASA, or AAS theorems") #Support for the ambiguous case needed
#--------------------Definitions of Theorems--------------------#
def SAS(Side1, Angle1, Side2): #Needs to use Law of Sines and Law of Cosines to be correct.
    

def SSS(Side1, Side2, Side3): #Needs to use Law of Cosines to find 3 angle values.
    s = (Side1 + Side2 + Side3)/2
    areaSSS = math.sqrt(s*(s - Side1)*(s - Side2)*(s - Side3))
    
    
def ASA(Angle1, Side1, Angle2):
    
#----------------------------------------------------------------#
input("Which theorem would you like to use? ")

