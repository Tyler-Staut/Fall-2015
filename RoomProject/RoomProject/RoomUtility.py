'''
Created on Sep 10, 2015

@author: Tyler
'''
#Imports----------
from math import *
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

room_1_area = 0
room_2_area = 0
room_3_area = 0
room_4_area = 0



def squareRoom(base, height):           #Used to define what the Square room area is
    return float(base * height)
    
#---------------WE HAVE ERROR HERE---------------
def semicircleRoom(radius):             #Used to define what the SemiCircle room area is
    return float((pi(radius)**2) / 4)
#------------------------------------------------
    
def triangleRoom(base, height):         #Used to define what the Triangle room area is
    return float((base * height) / 2)  


    
#--------------------USER INPUT--------------------

print("What shape do you want Room to be?\n")
#Room 1 Segment
def room1():
    while True:                         #Loop created to get info for Room 1
        room1 = str(input("Response: "))
        if room1 in ('Square', 'SemiCircle', 'Triangle'):
            if room1 == 'Square':                #This is for Square room
                base = float(input("Base: "))
                height = float(input("Height: "))
               
                
            elif room1 == 'SemiCircle':         #This is for Semi-SemiCircle room
                radius = float(input("Radius: "))
                semicircleRoom(radius)
                
                
            elif room1 == 'Triangle':           #This is for triangle room
                base = float(input("Base: "))
                height = float(input("Height: "))
                triangleRoom(base, height)
                
            break
        else:                   #Used to make it a loop until user inputs right response
            print('Input was Wrong. Try Again.')
        
        
#Room 2 Segment
def room2():
    while True:                 #Loop created to get info for Room 2
        room2 = str(input("What shape do you want Room 2 to be?\n"))
        if room2 in ('Square', 'SemiCircle', 'Triangle'):
            if room2 == 'Square':               #This is for Square room
                base = float(input("Base: "))
                height = float(input("Height: "))
                room_2_area = squareRoom(base, height)
                
            elif room2 == 'SemiCircle':         #This is for Semi-SemiCircle room
                radius = float(input("Radius: "))
                semicircleRoom(radius)
                room_2_area = semicircleRoom(radius)
                
            elif room2 == 'Triangle':           #This is for triangle room
                base = float(input("Base: "))
                height = float(input("Height: "))
                triangleRoom(base, height)
                room_2_area = triangleRoom(base, height)
            break
        else:                   #Used to make it a loop until user inputs right response
            print('Input was Wrong. Try Again.')
        
        
#Room 3 Segment
def room3():
    while True:                 #Loop created to get info for Room 3
        room3 = str(input("What shape do you want Room 3 to be?\n"))
        if room3 in ('Square', 'SemiCircle', 'Triangle'):
            if room3 == 'Square':               #This is for Square room
                base = float(input("Base: "))
                height = float(input("Height: "))
                room_3_area = squareRoom(base, height)
                
            elif room3 == 'SemiCircle':         #This is for Semi-SemiCircle room
                radius = float(input("Radius: "))
                semicircleRoom(radius)
                room_3_area = semicircleRoom(radius)
                
            elif room3 == 'Triangle':           #This is for triangle room
                base = float(input("Base: "))
                height = float(input("Height: "))
                triangleRoom(base, height)
                room_3_area = triangleRoom(base, height)
            break
        else:                   #Used to make it a loop until user inputs right response
            print('Input was Wrong. Try Again.')
        
        
#Room 4 Segment
def room4():
    while True:                 #Loop created to get info for Room 4
        room4 = str(input("What shape do you want Room 4 to be?\n"))
        if room4 in ('Square', 'SemiCircle', 'Triangle'):
            if room4 == 'Square':               #This is for Square room
                base = float(input("Base: "))
                height = float(input("Height: "))
                room_4_area = squareRoom(base, height)
                
            elif room4 == 'SemiCircle':         #This is for Semi-SemiCircle room
                radius = float(input("Radius: "))
                semicircleRoom(radius)
                room_4_area = semicircleRoom(radius)
                
            elif room4 == 'Triangle':           #This is for triangle room
                base = float(input("Base: "))
                height = float(input("Height: "))
                triangleRoom(base, height)
                room_4_area = triangleRoom(base, height)
            break
        else:                   #Used to make it a loop until user inputs right response
            print('Input was Wrong. Try Again.')


#-----------------------------------------------------
room1()
room2()
room3()
room4()

#Output
total_room_area = room_1_area + room_2_area + room_3_area + room_4_area


print(total_room_area)
