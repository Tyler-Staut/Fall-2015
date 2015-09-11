'''
Created on Sep 10, 2015

@author: Tyler
'''

from math import *



#Needed to define area
area = 0



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


room_1_area = 0
room_2_area = 0
room_3_area = 0
room_4_area = 0
    
    
    
#--------------------USER INPUT--------------------


def room():
    while True:
        print("What shape do you want this room to be?\n")  #Asks what room you want
        room = str(input("Response: "))
        if room in ('Square', 'SemiCircle', 'Triangle'):    #If room is in set then do the following
            if room == 'Square':                            #If square do:
                base = float(input("Base: "))
                height = float(input("Height: "))
                area = squareRoom(base, height)
                return area
                
            elif room1 == 'SemiCircle':                     #If SemiCircle do:
                radius = float(input("Radius: "))
                area = semicircleRoom(radius)
                return area
            elif room1 == 'Triangle':                       #If Triangle do:
                base = float(input("Base: "))
                height = float(input("Height: "))
                area = triangleRoom(base, height)
                return area
            break
        else:
            print('Input was Wrong. Try Again.')            #Not a correct input, go back through

        
        
#--------------------------------------------------

room()
room_1_area = area


room()
room_2_area = area


room()
room_3_area = area


room()
room_4_area = area

    



total_room_area = room_1_area + room_2_area + room_3_area + room_4_area

print("The total room area is: ", total_room_area)


