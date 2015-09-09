'''
Created on Sep 9, 2015

@author: Matt
'''
import math

print("Find all the info of your triangle!") 
print("You may choose from SAS, SSS, ASA, or AAS theorems") #Support for the ambiguous case needed

#Angles will eventually be converted into degrees in code for ease of use.

AngleA = 0
AngleB = 0
AngleC = 0
SideA = 0
SideB = 0
SideC = 0
areaSAS = 0
areaSSS = 0
areaASA = 0
AreaAAS = 0
s = 0
triangleTheorem = str(input("Which theorem would you like to use? "))

#--------------------Definitions of Theorems--------------------#
def SAS(SideA, AngleB, SideC): #Assume Angle C is the largest, and Angle A is smallest.
    areaSAS = float((SideA*SideC*math.sin(AngleB))/2)
    SideB = float(math.sqrt(SideA**2 + SideC**2 - 2*SideA*SideC*math.cos(AngleB)))
    AngleA = float(math.asin(SideA*math.sin(AngleB)/SideB))
    AngleC = float(math.pi - (AngleA + AngleB))
    print("Side B = ", SideB)
    print("Angle A = ", AngleA)
    print("Angle C = ", AngleC)
    print("Area = ", areaSAS)

def SSS(SideA, SideB, SideC): 
    s = (SideA + SideB + SideC)/2
    areaSSS = math.sqrt(s*(s - SideA)*(s - SideB)*(s - SideC))
    AngleA = math.acos((SideB**2 - SideA**2 + SideC**2)/2*SideB*SideC)
    AngleB = math.acos((SideA**2 - SideB**2 + SideC**2)/2*SideA*SideC)
    AngleC = math.acos((SideA**2 + SideB**2 - SideC**2)/2*SideA*SideB)
    print("Angle A = ", AngleA)
    print("Angle B = ", AngleB)
    print("Angle C = ", AngleC)
    print("Area = ", areaSSS)       
    
def ASA(AngleA, SideC, AngleB):
    AngleC = math.pi - (AngleA + AngleB)
    SideA = (SideC*math.sin(AngleA)/math.sin(AngleC))
    SideB = (SideC*math.sin(AngleB)/math.sin(AngleC))
    areaASA = (SideC**2*math.sin(AngleA)*math.sin(AngleB)/(2*math.sin(AngleC)))
    print("Angle C = ", AngleC)
    print("Side A = ", SideA)
    print("Side B = ", SideB)
    print("Area = ", areaASA)

def AAS(AngleA, AngleB, SideC): 
    AngleC = math.pi - (AngleA + AngleB)
    SideA = (SideC*math.sin(AngleA)/math.sin(AngleC))
    SideB = (SideC*math.sin(AngleB)/math.sin(AngleC))
    areaAAS = (SideC**2*math.sin(AngleA)*math.sin(AngleB)/(2*math.sin(AngleC)))
    print("Angle C = ", AngleC)
    print("Side A = ", SideA)
    print("Side B = ", SideB)
    print("Area = ", areaAAS)
#----------------------------------------------------------------#
if triangleTheorem in ('SAS', 'SSS', 'ASA', 'AAS'):
        if triangleTheorem == 'SAS':
            SideA = float(input("Side A: "))
            AngleB = float(input("Angle B (in radians): "))
            SideC = float(input("Side C: "))
            SAS(SideA, AngleB, SideC)
        elif triangleTheorem == 'SSS':
            SideA = float(input("Side A: "))
            SideB = float(input("Side B: "))
            SideC = float(input("Side C: "))
            SSS(SideA, SideB, SideC)
        elif triangleTheorem == 'ASA':
            AngleA = float(input("Angle A (in radians): "))
            SideC = float(input("Side C: "))
            AngleB = float(input("Angle B (in radians): "))
            ASA(AngleA, SideC, AngleB)
        elif triangleTheorem == 'AAS':
            AngleC = float(input("Angle C (in radians):"))
            SideA = float(input("Side A: "))
            SideB = float(input("Side B: "))
            AAS(AngleA, AngleB, SideC)
        
    
else:
    print("Input undefined; Try again.")
    
