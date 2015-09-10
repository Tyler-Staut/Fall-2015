'''
Created on Sep 9, 2015

@author: Matt
'''
import math

print("Find all the info of your triangle!") 
print("You may choose from SAS, SSS, ASA, or AAS theorems") #Support for the ambiguous case needed

#Angles will eventually be converted into degrees in code for ease of use.


#--------------------Definitions of Theorems--------------------#
def SAS(SideA, AngleB, SideC): #Assume Angle C is the largest, and Angle A is smallest.
    areaSAS = float((SideA*SideC*math.sin(AngleB))/2)
    SideB = float(math.sqrt(SideA**2 + SideC**2 - 2*SideA*SideC*math.cos(AngleB)))
    AngleA = float(math.asin(SideA*math.sin(AngleB)/SideB)*(180/math.pi))
    AngleC = float(math.asin(SideC*math.sin(AngleB)/SideB)*(180/math.pi))
    print("Side B = ", SideB, "units.")
    print("Angle A = ", AngleA, "degrees.")
    print("Angle C = ", AngleC, "degrees.")
    print("Area = ", areaSAS, "square units.")

def SSS(SideA, SideB, SideC): 
    s = (SideA + SideB + SideC)/2
    areaSSS = float(math.sqrt(s*(s - SideA)*(s - SideB)*(s - SideC)))
    AngleA = float(math.acos((SideB**2 - SideA**2 + SideC**2)/(2*SideB*SideC))*(180/math.pi))
    AngleB = float(math.acos((SideA**2 - SideB**2 + SideC**2)/(2*SideA*SideC))*(180/math.pi))
    AngleC = float(math.acos((SideA**2 + SideB**2 - SideC**2)/(2*SideA*SideB))*(180/math.pi))
    print("Angle A = ", AngleA, "degrees.")
    print("Angle B = ", AngleB, "degrees.")
    print("Angle C = ", AngleC, "degrees.")
    print("Area = ", areaSSS, "square units.")
    
def ASA(AngleA, SideC, AngleB):
    AngleC = float(math.pi - (AngleA + AngleB))*(180/math.pi)
    SideA = float((SideC*math.sin(AngleA)/math.sin((AngleC*(math.pi/180)))))
    SideB = float((SideC*math.sin(AngleB)/math.sin((AngleC*(math.pi/180)))))
    areaASA = float((SideC**2*math.sin(AngleA)*math.sin(AngleB)/(2*math.sin((AngleC*(math.pi/180))))))
    print("Angle C = ", AngleC, "degrees.")
    print("Side A = ", SideA, "units.")
    print("Side B = ", SideB, "units.")
    print("Area = ", areaASA, "square units.")

#AAS function under construction at the moment
def AAS(AngleA, AngleB, SideA): 
    AngleC = float(math.pi - (AngleA + AngleB))*(180/math.pi)
    SideC = float(SideA/(math.cos(AngleB)))
    SideB = float(SideA*math.tan(AngleB))
    areaAAS = float((SideC**2*math.sin(AngleA)*math.sin(AngleB)/(2*math.sin((AngleC*(math.pi/180))))))
    print("Angle C = ", AngleC, "degrees.")
    print("Side C = ", SideC, "units.")
    print("Side B = ", SideB, "units.")
    print("Area = ", areaAAS, "square units.")
#----------------------------------------------------------------#
triangleTheorem = str(input("Which theorem would you like to use? "))
if triangleTheorem in ('SAS', 'SSS', 'ASA', 'AAS'):
        if triangleTheorem == 'SAS':
            SideA = float(input("Side A: "))
            AngleB = float(input("Angle B (in degrees): "))*(math.pi/180)
            SideC = float(input("Side C: "))
            SAS(SideA, AngleB, SideC)
        elif triangleTheorem == 'SSS':
            print("The three sides must meet absolutely perfectly in order to work.")
            SideA = float(input("Side A: "))
            SideB = float(input("Side B: "))
            print("Length of Side C must be between ", float(math.sqrt(SideA**2 + SideB**2 - 2*SideA*SideB)), "and", float(math.sqrt(SideA**2 + SideB**2 + 2*SideA*SideB)))
            SideC = float(input("Side C: "))
            SSS(SideA, SideB, SideC)
        elif triangleTheorem == 'ASA':
            AngleA = float(input("Angle A (in degrees): "))*(math.pi/180)
            SideC = float(input("Side C: "))
            AngleB = float(input("Angle B (in degrees): "))*(math.pi/180)
            ASA(AngleA, SideC, AngleB)
        elif triangleTheorem == 'AAS':
            AngleA = float(input("Angle A (in degrees):"))*(math.pi/180)
            AngleB = float(input("Angle B (in degrees):"))*(math.pi/180)
            SideA = float(input("Side A: "))
            AAS(AngleA, AngleB, SideA)    
else:
    print("Input undefined; Try again.")
    
