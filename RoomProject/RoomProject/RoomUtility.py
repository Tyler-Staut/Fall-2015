'''
Created on Sep 10, 2015

@author: Tyler
'''

from math import *



#Needed to define area
area = 0
total_room_area = 0
roomArea = 0
#total_room_area = 0



#Used to define what the Square room area is
def squareRoom(base, height):
    roomArea = float(base * height)
    return roomArea
    
    
#Used to define what the SemiCircle room area is 
area2 = 0   
def semicircleRoom(radius):
    roomArea = (pi(radius)**2) / 4
    return roomArea
    
#Used to define what the Triangle room area is
area3 = 0    
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
                return roomArea
                
                
                
            elif room1 == 'SemiCircle':                     #If SemiCircle do:
                radius = float(input("Radius: "))
                roomArea = semicircleRoom(radius)
                total_room_area = total_room_area + roomArea
                
                
            elif room1 == 'Triangle':                       #If Triangle do:
                base = float(input("Base: "))
                height = float(input("Height: "))
                roomArea = triangleRoom(base, height)
                total_room_area = total_room_area + roomArea
                
                
            break
        else:
            print('Input was Wrong. Try Again.')            #Not a correct input, go back through

        
        
#--------------------------------------------------

room()
total_room_area = total_room_area + roomArea

room()
total_room_area = total_room_area + roomArea

room()
total_room_area = total_room_area + roomArea

room()
total_room_area = total_room_area + roomArea

print("The total room area is: ", total_room_area)


