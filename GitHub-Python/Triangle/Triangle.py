'''
Created on Sep 9, 2015

@author: Matt
'''
import math

print("Find all the info of your triangle!") 
print("You may choose from SAS, SSS, ASA, or AAS theorems") #Support for the ambiguous case needed
#--------------------Definitions of Theorems--------------------#
def SAS(SideA, AngleB, SideC): #Assume Angle C is the largest, and Angle A is smallest.
    areaSAS = (SideA*SideC*math.sin(AngleB))/2
    SideB = math.sqrt(SideA**2 + SideC**2 - 2*SideA*SideC*math.cos(AngleB))
    AngleA = math.asin(SideA*math.sin(AngleB)/SideB)
    AngleC = math.pi - (AngleA + AngleB)
    
    

def SSS(SideA, SideB, SideC): #Needs to use Law of Cosines to find 3 angle values.
    s = (SideA + SideB + SideC)/2
    areaSSS = math.sqrt(s*(s - SideA)*(s - SideB)*(s - SideC))
    AngleA = math.acos((SideB**2 - SideA**2 + SideC**2)/2*SideB*SideC)
    AngleB = math.acos((SideA**2 - SideB**2 + SideC**2)/2*SideA*SideC)
    AngleC = math.acos((SideA**2 + SideB**2 - SideC**2)/2*SideA*SideB)
       
    
def ASA(AngleA, SideC, AngleB):
    AngleC = math.pi - (AngleA + AngleB)
    SideA = (SideC*math.sin(AngleA)/math.sin(AngleC))
    SideB = (SideC*math.sin(AngleB)/math.sin(AngleC))
    areaASA = (SideC**2*math.sin(AngleA)*math.sin(AngleB)/(2*math.sin(AngleC)))
    

    
    
    
#----------------------------------------------------------------#
input("Which theorem would you like to use? ")

