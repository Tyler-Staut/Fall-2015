'''
Created on Sep 10, 2015

@author: Tyler
'''
#Imports----------
from math import *
from tkinter.constants import YES
#-----------------
'''
#--------------------BASE CODE-----------------------

W = float(input("W= "))
X = float(input("X= "))
Y = float(input("Y= "))
Z = float(input("Z= "))
print('\n')                 #Spaces put between text so I can read info better
print("Angle of A must be between", 
      (atan(W/Z))/pi ,"pi and", 
      (pi - atan(W/Z))/pi , "pi")    #Made this span multiple lines so I can read it better.
A = pi * float(input("Angle of A = pi * "))
S = float(W/tan(A))
L = float(Z-S)
T = float(sqrt(W**2 + S**2))

print('\n')                 #Spaces put between text so I can read info better
print("L = ", L)
print("S = ", S)
print('\n')                 #Spaces put between text so I can read info better
#-------------------------------------------------------
'''






def squareRoom(base, height):           #Used to define what the Square room area is
    return float(base * height)
    
#---------------WE HAVE ERROR HERE---------------
def semicircleRoom(radius):             #Used to define what the SemiCircle room area is
    return float((pi(radius)**2) / 4)
#------------------------------------------------
    
def triangleRoom(base, height):         #Used to define what the Triangle room area is
    return float((base * height) / 2)  


    
#--------------------USER INPUT--------------------


        

def room():
    room = str(input("What shape do you want room " + str(roomnum) + " to be.\n"))
    if room in ('Square', 'SemiCircle', 'Triangle'):
        if room == 'Square':               #This is for Square room
            base = float(input("Base: "))
            height = float(input("Height: "))
            area = squareRoom(base, height)
            return area
            
        elif room == 'SemiCircle':         #This is for Semi-SemiCircle room
            radius = float(input("Radius: "))
            area = semicircleRoom(radius)
            return area
        elif room == 'Triangle':           #This is for triangle room
            base = float(input("Base: "))
            height = float(input("Height: "))
            area = triangleRoom(base, height)
            return area
            
    else:
        print('Input was Wrong. Try Again.')
print("\n")

#-----------------------------------------------------
val1=0
val2=0
val3=0
val4=0


def values():
    roomnum=1
    room()
    area=val1
    
    roomnum=roomnum+1
    room()
    area=val2
    
    roomnum=roomnum+1
    room()
    area=val3
    
    roomnum=roomnum+1
    room()
    area=val4

def total_room_area():
    print(total_room_area)

def restart():
    yes=str("yes")
    no=str("no")
    restart = input("Restart?")
    if restart == str(yes):
        runprogram()
    elif restart == no:
        exit()
    
    
def runprogram():
    values()
    print(val1)
    print(val2)
    print(val3)
    print(val4)
    total_room_area()
    restart()
#Output


runprogram()

