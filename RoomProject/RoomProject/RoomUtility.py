'''
Created on Sep 10, 2015

@author: Tyler
'''

from math import *



#------LISTS-----
roomAreas = []
#----------------


numRooms = int(input("How many rooms do you want to have? "))

#Used to define what the Square room area is
def squareRoom(base, height):
    roomArea = float(base * height)
    return roomArea
    
    
#Used to define what the SemiCircle room area is   
def semicircleRoom(radius):
    roomArea = (pi(radius)**2) / 4
    return roomArea
    
#Used to define what the Triangle room area is 
def triangleRoom(base, height):
    roomArea = (base * height) / 2
    return roomArea
    
#Used to define the different rooms



    
    
#--------------------USER INPUT--------------------


def room():
    while True:
        
        print("What shape do you want this room to be?\n")  #Asks what room you want
        room = str(input("Response: "))
        if room in ('Square', 'SemiCircle', 'Triangle'):    #If room is in set then do the following
            if room == 'Square':                            #If square do:
                base = float(input("Base: "))
                height = float(input("Height: "))
                roomArea = squareRoom(base, height)
                roomAreas.append(roomArea)
                
                
                
                
            elif room == 'SemiCircle':                     #If SemiCircle do:
                radius = float(input("Radius: "))
                roomArea = semicircleRoom(radius)
                total_room_area = total_room_area + roomArea
                roomAreas.append(roomArea)
                
                
            elif room == 'Triangle':                       #If Triangle do:
                base = float(input("Base: "))
                height = float(input("Height: "))
                roomArea = triangleRoom(base, height)
                total_room_area = total_room_area + roomArea
                roomAreas.append(roomArea)
                
                
            break
        else:
            print('Input was Wrong. Try Again.')            #Not a correct input, go back through

        
        
#--------------------------------------------------

def runProgram():
    for i in range(numRooms):
        room()
        
runProgram()

print("The total area in each room is as follows: ")
x = 1
for i in range(numRooms):
    print("Room %d is:" % x, roomAreas[i])
    x = x + 1


